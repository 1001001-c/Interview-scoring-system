<template>
    <div class="container mt-4">
        <h2 class="mb-4 text-center">考试设置</h2>
        <form @submit.prevent="submitForm" class="needs-validation" novalidate>
            <div class="row mb-3">
                <div class="col-md-6">
                    <label for="examName" class="form-label">考试项目名称:</label>
                    <input type="text" v-model="form.examName" class="form-control" id="examName" required />
                    <div class="invalid-feedback">请输入考试项目名称</div>
                </div>
                <div class="col-md-6">
                    <label for="numExams" class="form-label">考场数量:</label>
                    <input type="number" v-model.number="form.numExams" class="form-control" id="numExams" min="1" required />
                    <div class="invalid-feedback">请输入有效的考场数量</div>
                </div>
            </div>

            <div class="row mb-3">
                <div class="col-md-6">
                    <label for="judgesRange" class="form-label">每个考场的评委数范围:</label>
                    <input type="text" v-model="form.judgesRange" class="form-control" id="judgesRange" placeholder="例如: 3-5" required />
                    <div class="invalid-feedback">请输入评委数范围</div>
                </div>
                <div class="col-md-6">
                    <label for="studentsPerRound" class="form-label">每轮考生数:</label>
                    <input type="number" v-model.number="form.studentsPerRound" class="form-control" id="studentsPerRound" min="1" required />
                    <div class="invalid-feedback">请输入有效的每轮考生数</div>
                </div>
            </div>

            <div v-for="(position, index) in form.examPositions" :key="index" class="row mb-3">
                <div class="col-md-5">
                    <label for="examCode" class="form-label">报考岗位代码:</label>
                    <input type="text" v-model="position.code" class="form-control" required />
                    <div class="invalid-feedback">请输入报考岗位代码</div>
                </div>
                <div class="col-md-5">
                    <label for="questions" class="form-label">考题列表 (逗号分隔):</label>
                    <input type="text" v-model="position.questions" class="form-control" placeholder="考题列表" />
                </div>
                <div class="col-md-2 d-flex align-items-end">
                    <button type="button" class="btn btn-outline-danger" @click="removeExamPosition(index)">删除</button>
                </div>
            </div>
            <button type="button" class="btn btn-outline-primary" @click="addExamPosition">添加报考岗位</button>

            <div class="mb-3">
                <label class="form-label">打分项:</label>
                <div v-for="(item, index) in form.scoringItems" :key="index" class="mb-3">
                    <div class="input-group">
                        <input type="text" v-model="item.name" class="form-control" placeholder="评分项名称" required />
                        <input type="number" v-model.number="item.score" class="form-control" placeholder="分值" min="0" required />
                        <input type="text" v-model="item.criteria" class="form-control" placeholder="评分标准" />
                        <button type="button" class="btn btn-outline-danger" @click="removeScoringItem(index)">删除</button>
                    </div>
                </div>
                <button type="button" class="btn btn-outline-primary" @click="addScoringItem">添加打分项</button>
            </div>

            <button type="submit" class="btn btn-success" :disabled="isSubmitting">提交</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            form: this.getDefaultForm(),
            isSubmitting: false,
        };
    },
    methods: {
        getDefaultForm() {
            return {
                examName: '',
                numExams: 0,
                judgesRange: '',
                studentsPerRound: 0,
                examPositions: [{ code: '', questions: '' }],
                scoringItems: [{ name: '', score: 0, criteria: '' }],
            };
        },
        addExamPosition() {
            this.form.examPositions.push({ code: '', questions: '' });
        },
        removeExamPosition(index) {
            this.form.examPositions.splice(index, 1);
        },
        addScoringItem() {
            this.form.scoringItems.push({ name: '', score: 0, criteria: '' });
        },
        removeScoringItem(index) {
            this.form.scoringItems.splice(index, 1);
        },
        async submitForm() {
            this.isSubmitting = true;
            try {
                const response = await axios.post('http://localhost:8000/api/exams/', this.form);
                console.log('提交成功:', response.data);
                // 重置表单
                this.form = this.getDefaultForm();
            } catch (error) {
                console.error('提交失败:', error.response ? error.response.data : error.message);
            } finally {
                this.isSubmitting = false;
            }
        },
    },
};
</script>

<style scoped>
.text-center {
    text-align: center;
}

.btn {
    width: auto;
    padding: 0.5rem 2rem;
    margin-top: 1rem;
}

.form-control {
    margin-bottom: 1rem;
}
</style>
