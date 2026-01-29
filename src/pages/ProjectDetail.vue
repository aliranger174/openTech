<template>
  <div class="project-detail">
    <button class="back-btn" @click="goBack">← بازگشت</button>
    
    <div v-if="project" class="project-container">
      <div class="header">
        <div class="header-top">
          <div class="project-icon">{{ project.icon }}</div>
          <div class="title-section">
            <h1>{{ project.title }}</h1>
            <span class="status" :class="project.status.toLowerCase()">{{ project.status }}</span>
          </div>
        </div>
      </div>

      <div class="content">
        <div class="description-section">
          <h3>توضیحات</h3>
          <p>{{ project.description }}</p>
        </div>

        <div class="info-grid">
          <div class="info-card">
            <p class="label">دسته‌بندی</p>
            <p class="value">{{ project.category }}</p>
          </div>
          <div class="info-card">
            <p class="label">تاریخ</p>
            <p class="value">{{ project.date }}</p>
          </div>
        </div>

        <div class="technologies-section">
          <h3>تکنولوژی‌های استفاده شده</h3>
          <div class="tech-list">
            <span v-for="tech in project.technologies" :key="tech" class="tech-tag">
              {{ tech }}
            </span>
          </div>
        </div>

        <button class="btn-view">مشاهده پروژه</button>
      </div>
    </div>

    <div v-else class="not-found">
      پروژه یافت نشد
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectDetail',
  data() {
    return {
      projectsData: [
        {
          id: 1,
          title: 'پلتفرم اخبار تکنولوژی',
          description: 'وبسایت منابع اخبار و آموزش تکنولوژی با طراحی مدرن.',
          category: 'وب',
          icon: '📰',
          technologies: ['Vue.js', 'Vite', 'CSS3'],
          date: 'دسامبر ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 2,
          title: 'اپ یادگیری لینوکس',
          description: 'اپلیکیشن موبایل برای یادگیری دستورات لینوکس.',
          category: 'موبایل',
          icon: '🐧',
          technologies: ['React Native', 'Node.js', 'MongoDB'],
          date: 'نوامبر ۲۰۲۵',
          status: 'درحال‌توسعه'
        },
        {
          id: 3,
          title: 'ابزار تحلیل امنیت',
          description: 'ابزار خط‌فرمانی برای بررسی امنیت وبسایت‌ها.',
          category: 'ابزار',
          icon: '🔒',
          technologies: ['Python', 'Bash', 'Linux'],
          date: 'اکتبر ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 4,
          title: 'داشبورد مدیریتی',
          description: 'داشبورد مدیریتی برای نظارت بر سرورهای لینوکس.',
          category: 'وب',
          icon: '📊',
          technologies: ['Vue.js', 'Express', 'WebSocket'],
          date: 'سپتامبر ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 5,
          title: 'کتاب‌خانه کمپایلر',
          description: 'کتاب‌خانه برای ساخت و تحلیل کمپایلرهای ساده.',
          category: 'ابزار',
          icon: '⚙️',
          technologies: ['C++', 'LLVM', 'Parser'],
          date: 'آگوست ۲۰۲۵',
          status: 'درحال‌توسعه'
        }
      ]
    }
  },
  computed: {
    project() {
      const id = parseInt(this.$route.params.id)
      return this.projectsData.find(p => p.id === id)
    }
  },
  methods: {
    goBack() {
      this.$router.back()
    }
  }
}
</script>

<style scoped>
.project-detail {
  max-width: 900px;
  margin: 0 auto;
  color: white;
}

.back-btn {
  background: none;
  border: none;
  color: #a78bfa;
  cursor: pointer;
  font-size: 16px;
  margin-bottom: 24px;
  transition: color 0.3s;
}

.back-btn:hover {
  color: #06b6d4;
}

.project-container {
  background: rgba(124, 58, 237, 0.1);
  padding: 40px;
  border-radius: 12px;
  border: 1px solid rgba(124, 58, 237, 0.3);
  backdrop-filter: blur(10px);
}

.header-top {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 32px;
}

.project-icon {
  font-size: 64px;
  min-width: 80px;
  text-align: center;
}

.title-section h1 {
  font-size: 32px;
  margin: 0 0 12px 0;
  line-height: 1.4;
}

.status {
  display: inline-block;
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  color: white;
}

.status.فعال {
  background: #27ae60;
}

.status.درحال‌توسعه {
  background: #f39c12;
}

.description-section {
  margin-bottom: 32px;
  padding-bottom: 24px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.description-section h3 {
  margin-bottom: 12px;
  font-size: 18px;
}

.description-section p {
  line-height: 1.6;
  opacity: 0.9;
  margin: 0;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 32px 0;
}

.info-card {
  background: rgba(255, 255, 255, 0.05);
  padding: 16px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.label {
  font-size: 12px;
  opacity: 0.7;
  margin: 0 0 8px 0;
}

.value {
  font-size: 16px;
  font-weight: 600;
  margin: 0;
}

.technologies-section {
  margin: 32px 0;
  padding: 24px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.technologies-section h3 {
  margin-bottom: 16px;
  font-size: 18px;
}

.tech-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tech-tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 8px 16px;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  color: white;
}

.btn-view {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  color: white;
  padding: 12px 32px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  font-size: 16px;
  transition: all 0.3s;
}

.btn-view:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.not-found {
  text-align: center;
  padding: 40px;
  opacity: 0.6;
  font-size: 18px;
}

@media (max-width: 768px) {
  .project-container {
    padding: 24px;
  }

  .header-top {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }

  .title-section h1 {
    font-size: 24px;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }
}
</style>
