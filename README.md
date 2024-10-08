# Interview-scoring-system
### 1. 用户管理模块
- **模型设计**：
  - 使用 Django 自带的 `User` 模型扩展，创建 `UserProfile` 模型，包含用户名、密码、角色（管理员、主考、辅考、考务、评委等）以及其他个人信息。

- **功能实现**：
  - 用户名根据拼音生成，密码默认为身份证后六位。如用户名重复，自动在用户名后添加数字区分。
  - 管理员通过 Django Admin 或自定义管理页面创建和管理账户。

### 2. 考试项目管理模块
- **模型设计**：
  - 创建 `ExamProject` 模型：包括考试项目名称、考场数量、报考岗位代码等。
  - 创建 `ExamRoom` 模型：包括评委人数范围、每轮考生数等。
  - 创建 `ScoreItem` 模型：包括打分项名称、分值、评分标准等。

- **功能实现**：
  - 通过表单视图输入考试项目信息和考场设置。
  - 录入评委和考生的信息，分配账号和初始密码。
  - 使用 Django signals 或自定义逻辑实现考生和评委的自动或手动分配。

### 3. 考试流程管理模块
- **模型设计**：
  - 创建 `InterviewSession` 模型，用于记录每轮面试的具体情况，如考生到场情况和缺考标记。

- **功能实现**：
  - 考务人员通过登录页面进入考场管理。
  - 面试开始后，通过 JavaScript 实现倒计时功能。
  - 记录面试过程中的各类数据，包括考生的到场和缺考情况。

### 4. 打分管理模块
- **模型设计**：
  - 创建 `Score` 模型，记录评委对每个考生在各个打分项上的评分，并保留修改前后的打分记录。

- **功能实现**：
  - 评委登录后可以进行打分，并确认和提交打分结果。
  - 考务人员可以在后台进行打分修改，并保留修改记录。
  - 根据打分规则计算最终成绩，生成 PDF 或 Word 格式的成绩报告。

### 5. 实时监控模块
- **模型设计**：
  - 不需要 WebSocket，直接通过查询数据库监控已提交的打分数据。

- **功能实现**：
  - 后端提供一个视图，用于返回最新的打分数据。
  - 前端页面通过 JavaScript（如 jQuery）定时发送 AJAX 请求，获取最新数据并更新页面，实现实时监控。
  - 页面设计为表格或图表形式，展示各考场或考生的打分情况。

### 整体流程
1. **用户管理模块**：管理员创建和管理系统用户，设置用户权限。
2. **考试项目管理模块**：创建和管理考试项目，分配考生和评委到考场和轮次。
3. **考试流程管理模块**：记录并管理面试过程中的考生情况，控制面试流程。
4. **打分管理模块**：评委对考生进行打分，考务人员管理和修改打分数据，生成最终成绩报告。
5. **实时监控模块**：定时刷新页面显示已提交的打分数据，供主考和辅考监控各考场情况。

