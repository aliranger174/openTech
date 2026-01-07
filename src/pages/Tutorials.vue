<template>
  <div class="tutorials-page">
    <h2>آموزش‌ها</h2>
    
    <div class="filter-tabs">
      <button 
        v-for="category in categories"
        :key="category"
        @click="selectedCategory = category"
        :class="{ active: selectedCategory === category }"
        class="tab"
      >
        {{ category }}
      </button>
    </div>

    <div class="tutorials-grid">
      <div 
        v-for="tutorial in filteredTutorials" 
        :key="tutorial.id"
        class="tutorial-card"
      >
        <div class="level" :class="tutorial.level.toLowerCase()">
          {{ tutorial.level }}
        </div>
        <h3>{{ tutorial.title }}</h3>
        <p>{{ tutorial.description }}</p>
        <div class="meta">
          <span>{{ tutorial.duration }} ساعت</span>
          <span>{{ tutorial.lessons }} درس</span>
        </div>
        <button class="start-btn">شروع</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Tutorials',
  data() {
    return {
      selectedCategory: 'همه',
      categories: ['همه', 'لینوکس', 'امنیت', 'برنامه‌نویسی', 'DevOps'],
      tutorials: [
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
        },
        {
          id: 7,
          title: 'امنیت سایبری مبتدی',
          description: 'اصول بنیادی امنیت.',
          category: 'امنیت',
          level: 'مبتدی',
          duration: 9,
          lessons: 22
        },
        {
          id: 8,
          title: 'Kubernetes',
          description: 'مدیریت اپلیکیشن‌ها.',
          category: 'DevOps',
          level: 'پیشرفته',
          duration: 18,
          lessons: 40
        }
      ]
    }
  },
  computed: {
    filteredTutorials() {
      if (this.selectedCategory === 'همه') {
        return this.tutorials
      }
      return this.tutorials.filter(t => t.category === this.selectedCategory)
    }
  }
}
</script>

<style scoped>
.tutorials-page {
  color: white;
  max-width: 1200px;
  margin: 0 auto;
}

.tutorials-page h2 {
  font-size: 36px;
  margin-bottom: 24px;
  text-align: center;
  font-weight: 700;
}

.filter-tabs {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.tab {
  padding: 8px 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  background: transparent;
  color: white;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 13px;
  font-weight: 500;
}

.tab:active {
  border-color: white;
  background: rgba(255, 255, 255, 0.1);
}

.tab.active {
  background: white;
  color: #667eea;
  border-color: white;
}

.tutorials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}

.tutorial-card {
  background: rgba(255, 255, 255, 0.08);
  padding: 20px;
  border-radius: 8px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  position: relative;
}

.tutorial-card:active {
  background: rgba(255, 255, 255, 0.12);
  transform: translateY(-3px);
}

.level {
  position: absolute;
  top: 12px;
  right: 12px;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 11px;
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

.tutorial-card h3 {
  font-size: 15px;
  margin-bottom: 8px;
  margin-top: 24px;
  line-height: 1.4;
  font-weight: 600;
}

.tutorial-card p {
  font-size: 12px;
  opacity: 0.75;
  margin-bottom: 12px;
  flex-grow: 1;
  line-height: 1.5;
}

.meta {
  display: flex;
  gap: 16px;
  margin-bottom: 12px;
  font-size: 12px;
  opacity: 0.6;
}

.start-btn {
  padding: 10px 16px;
  background: white;
  color: #667eea;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 12px;
}

.start-btn:active {
  transform: scale(0.95);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

@media (max-width: 768px) {
  .tutorials-page h2 {
    font-size: 24px;
  }
  
  .filter-tabs {
    justify-content: flex-start;
    overflow-x: auto;
    gap: 8px;
  }
  
  .tutorials-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .tutorials-grid {
    grid-template-columns: 1fr;
  }
  
  .tutorial-card {
    padding: 16px;
  }
}
</style>
