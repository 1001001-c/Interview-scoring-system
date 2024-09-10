<template>
    <div class="container mt-4">
      <h2 class="text-center mb-4">提交的考试数据</h2>
      <div class="submitted-data">
        <h3>考试名称: {{ formData.exam_name }}</h3>
        <p>考场数量: {{ formData.num_exams }}</p>
        <p>评委数范围: {{ formData.judges_range }}</p>
        <p>每轮考生数: {{ formData.students_per_round }}</p>
  
        <h4>报考岗位:</h4>
        <ul>
          <li v-for="(position, index) in formData.exam_positions" :key="index">
            岗位代码: {{ position.code }} - 考题: {{ position.questions }}
          </li>
        </ul>
  
        <h4>打分项:</h4>
        <ul>
          <li v-for="(item, index) in formData.scoring_items" :key="index">
            {{ item.name }} - 分值: {{ item.score }} - 评分标准: {{ item.criteria }}
          </li>
        </ul>
  
        <!-- 文件上传区域 -->
        <h4>上传文件:</h4>
        <div class="file-upload">
          <label for="examinersFile">上传评委信息文件:</label>
          <input type="file" id="examinersFile" @change="handleExaminersFileUpload" accept=".csv">
          <p v-if="examinersFileName">已选择文件: {{ examinersFileName }}</p>
  
          <label for="candidatesFile">上传学生信息文件:</label>
          <input type="file" id="candidatesFile" @change="handleCandidatesFileUpload" accept=".csv">
          <p v-if="candidatesFileName">已选择文件: {{ candidatesFileName }}</p>
        </div>
  
        <!-- 提交按钮 -->
        <button class="btn btn-outline-primary mt-3" @click="submitFiles">提交文件</button>
  
        <!-- 返回按钮 -->
        <button class="btn btn-outline-secondary mt-2" @click="goBack">返回</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';  // 需要安装 axios： npm install axios
  
  export default {
    data() {
      return {
        formData: JSON.parse(this.$route.query.formData),
        examinersFile: null,  // 保存评委文件对象
        candidatesFile: null,  // 保存学生文件对象
        examinersFileName: '',  // 显示评委文件名称
        candidatesFileName: ''  // 显示学生文件名称
      };
    },
    methods: {
      // 处理评委文件上传
      handleExaminersFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.examinersFile = file;
          this.examinersFileName = file.name;
        }
      },
      // 处理学生文件上传
      handleCandidatesFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
          this.candidatesFile = file;
          this.candidatesFileName = file.name;
        }
      },
      // 提交文件
      async submitFiles() {
        if (!this.examinersFile || !this.candidatesFile) {
          alert("请上传所有文件后再提交！");
          return;
        }
  
        // 构建 FormData 对象
        const formData = new FormData();
        formData.append('examiners_file', this.examinersFile);
        formData.append('candidates_file', this.candidatesFile);
  
        try {
          // 使用 axios 发送 POST 请求到后端 API
          const response = await axios.post('/upload-files/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          });
  
          // 处理成功响应
          alert(response.data.status);
        } catch (error) {
          // 处理错误响应
          alert("文件上传失败：" + error.response.data.error || "未知错误");
        }
      },
      // 返回到上一个页面
      goBack() {
        this.$router.push({ name: 'ExamSettingsPage' });
      }
    }
  };
  </script>
  
  <style scoped>
  .text-center {
    text-align: center;
  }
  .submitted-data {
    margin: 1rem 0;
  }
  ul {
    list-style: none;
    padding: 0;
  }
  ul li {
    margin-bottom: 1rem;
  }
  .file-upload {
    margin-top: 1rem;
  }
  </style>
  