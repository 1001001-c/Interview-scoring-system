
from rest_framework import serializers
from .models import Exam, ExamPosition, ScoringItem

class ExamPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPosition
        fields = ['id', 'code', 'questions']

class ScoringItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringItem
        fields = ['id', 'name', 'score', 'criteria']

class ExamSerializer(serializers.ModelSerializer):
    exam_positions = ExamPositionSerializer(many=True)
    scoring_items = ScoringItemSerializer(many=True)

    class Meta:
        model = Exam
        fields = [
            'id',
            'exam_name',
            'num_exams',
            'judges_range',
            'students_per_round',
            'exam_positions',
            'scoring_items',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        exam_positions_data = validated_data.pop('exam_positions')
        scoring_items_data = validated_data.pop('scoring_items')
        
        exam = Exam.objects.create(**validated_data)
        
        for position_data in exam_positions_data:
            ExamPosition.objects.create(exam=exam, **position_data)
        
        for scoring_data in scoring_items_data:
            ScoringItem.objects.create(exam=exam, **scoring_data)
        
        return exam

    def update(self, instance, validated_data):
        exam_positions_data = validated_data.pop('exam_positions', [])
        scoring_items_data = validated_data.pop('scoring_items', [])

        # 更新 Exam 基本字段
        instance.exam_name = validated_data.get('exam_name', instance.exam_name)
        instance.num_exams = validated_data.get('num_exams', instance.num_exams)
        instance.judges_range = validated_data.get('judges_range', instance.judges_range)
        instance.students_per_round = validated_data.get('students_per_round', instance.students_per_round)
        instance.save()

        # 更新 ExamPosition
        self._update_exam_positions(instance, exam_positions_data)

        # 更新 ScoringItem
        self._update_scoring_items(instance, scoring_items_data)

        return instance

    def _update_exam_positions(self, exam, positions_data):
        existing_positions = {position.id: position for position in exam.exam_positions.all()}
        incoming_positions = []

        for position_data in positions_data:
            position_id = position_data.get('id', None)
            if position_id and position_id in existing_positions:
                position = existing_positions.pop(position_id)
                position.code = position_data.get('code', position.code)
                position.questions = position_data.get('questions', position.questions)
                position.save()
            else:
                ExamPosition.objects.create(exam=exam, **position_data)
        
        # 删除未在 incoming_positions 中的旧数据
        for position in existing_positions.values():
            position.delete()

    def _update_scoring_items(self, exam, scoring_data):
        existing_items = {item.id: item for item in exam.scoring_items.all()}
        incoming_items = []

        for item_data in scoring_data:
            item_id = item_data.get('id', None)
            if item_id and item_id in existing_items:
                item = existing_items.pop(item_id)
                item.name = item_data.get('name', item.name)
                item.score = item_data.get('score', item.score)
                item.criteria = item_data.get('criteria', item.criteria)
                item.save()
            else:
                ScoringItem.objects.create(exam=exam, **item_data)
        
        # 删除未在 incoming_items 中的旧数据
        for item in existing_items.values():
            item.delete()