<template>
  <div class="tutorial-detail">
    <button class="back-btn" @click="goBack">← بازگشت</button>
    
    <div v-if="tutorial" class="tutorial-container">
      <div class="header">
        <h1>{{ tutorial.title }}</h1>
        <div class="meta">
          <span class="level" :class="tutorial.level.toLowerCase()">{{ tutorial.level }}</span>
          <span class="category">{{ tutorial.category }}</span>
        </div>
      </div>

      <div class="content">
        <div class="info-grid">
          <div class="info-card">
            <div class="icon">⏱️</div>
            <div class="info-text">
              <p class="label">مدت زمان</p>
              <p class="value">{{ tutorial.duration }} ساعت</p>
            </div>
          </div>
          <div class="info-card">
            <div class="icon">📚</div>
            <div class="info-text">
              <p class="label">تعداد درس</p>
              <p class="value">{{ tutorial.lessons }} درس</p>
            </div>
          </div>
        </div>

        <div class="description">
          <h3>توضیحات</h3>
          <p>{{ tutorial.description }}</p>
        </div>

        <button class="btn-start">شروع یادگیری</button>
      </div>
    </div>

    <div v-else class="not-found">
      آموزش یافت نشد
    </div>
  </div>
</template>

<script>
export default {
  name: 'TutorialDetail',
  data() {
    return {
      tutorialsData: [
        {
          id: 1,
          title: 'مقدمه لینوکس',
          description: 'یاد بگیرید لینوکس را نصب و استفاده کنید.',
          category: 'لینوکس',
          level: 'مبتدی',
          duration: 10,
          lessons: 25
        },
        {
          id: 2,
          title: 'امنیت لینوکس پیشرفته',
          description: 'تکنیک‌های پیشرفته برای تامین امنیت.',
          category: 'امنیت',
          level: 'پیشرفته',
          duration: 15,
          lessons: 30
        },
        {
          id: 3,
          title: 'Bash Scripting',
          description: 'نوشتن script‌های قدرتمند bash.',
          category: 'برنامه‌نویسی',
          level: 'متوسط',
          duration: 8,
          lessons: 20
        },
        {
          id: 4,
          title: 'Docker و Container‌ها',
          description: 'درک کامل Docker.',
          category: 'DevOps',
          level: 'متوسط',
          duration: 12,
          lessons: 28
        },
        {
          id: 5,
          title: 'Vue.js برای مبتدیان',
          description: 'آموزش کامل Vue.js.',
          category: 'برنامه‌نویسی',
          level: 'مبتدی',
          duration: 14,
          lessons: 35
        },
        {
          id: 6,
          title: 'Node.js و Express',
          description: 'ساخت API‌های RESTful.',
          category: 'برنامه‌نویسی',
          level: 'متوسط',
          duration: 11,
          lessons: 26
        }
      ]
    }
  },
  computed: {
    tutorial() {
      const id = parseInt(this.$route.params.id)
      return this.tutorialsData.find(t => t.id === id)
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
.tutorial-detail {
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

.tutorial-container {
  background: rgba(124, 58, 237, 0.1);
  padding: 40px;
  border-radius: 12px;
  border: 1px solid rgba(124, 58, 237, 0.3);
  backdrop-filter: blur(10px);
}

.header h1 {
  font-size: 32px;
  margin-bottom: 16px;
  line-height: 1.4;
}

.meta {
  display: flex;
  gap: 16px;
  align-items: center;
  margin-bottom: 32px;
}

.level {
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  color: white;
}

.level.مبتدی {
  background: #27ae60;
}

.level.متوسط {
  background: #f39c12;
}

.level.پیشرفته {
  background: #e74c3c;
}

.category {
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  background: rgba(124, 58, 237, 0.6);
  color: white;
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 32px 0;
}

.info-card {
  background: rgba(255, 255, 255, 0.05);
  padding: 20px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  gap: 16px;
  align-items: center;
}

.icon {
  font-size: 32px;
}

.info-text {
  flex: 1;
}

.label {
  font-size: 12px;
  opacity: 0.7;
  margin: 0;
}

.value {
  font-size: 20px;
  font-weight: 600;
  margin: 0;
}

.description {
  margin: 32px 0;
  padding: 24px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.description h3 {
  margin-bottom: 12px;
  font-size: 18px;
}

.description p {
  line-height: 1.6;
  opacity: 0.9;
  margin: 0;
}

.btn-start {
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

.btn-start:hover {
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
  .tutorial-container {
    padding: 24px;
  }

  .header h1 {
    font-size: 24px;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }
}
</style>
