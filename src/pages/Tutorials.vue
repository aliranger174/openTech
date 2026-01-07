<template>
  <div class="tutorials-page">
    <div class="container">
      <h2>آموزش‌های تخصصی</h2>
      
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
          <p class="description">{{ tutorial.description }}</p>
          <div class="meta">
            <span class="duration">⏱️ {{ tutorial.duration }} ساعت</span>
            <span class="lessons">📚 {{ tutorial.lessons }} درس</span>
          </div>
          <button class="start-btn">شروع کنید</button>
        </div>
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
      categories: ['همه', 'لینوکس', 'امنیت', 'برنامه‌نویسی', 'DevOps', 'وب'],
      tutorials: [
        {
          id: 1,
          title: 'مقدمه‌ای بر لینوکس',
          description: 'یاد بگیرید لینوکس را نصب و استفاده کنید. از خط فرمان تا مدیریت سیستم.',
          category: 'لینوکس',
          level: 'مبتدی',
          duration: 10,
          lessons: 25
        },
        {
          id: 2,
          title: 'امنیت لینوکس پیشرفته',
          description: 'تکنیک‌های پیشرفته برای تامین امنیت سیستم‌های لینوکس.',
          category: 'امنیت',
          level: 'پیشرفته',
          duration: 15,
          lessons: 30
        },
        {
          id: 3,
          title: 'Bash Scripting از صفر تا قهرمان',
          description: 'نوشتن script‌های قدرتمند bash برای خودکارسازی کارها.',
          category: 'برنامه‌نویسی',
          level: 'متوسط',
          duration: 8,
          lessons: 20
        },
        {
          id: 4,
          title: 'Docker و Container‌ها',
          description: 'درک کامل Docker و استفاده از Container‌ها در توسعه.',
          category: 'DevOps',
          level: 'متوسط',
          duration: 12,
          lessons: 28
        },
        {
          id: 5,
          title: 'Vue.js برای مبتدیان',
          description: 'آموزش کامل Vue.js و ساخت اپلیکیشن‌های تعاملی.',
          category: 'وب',
          level: 'مبتدی',
          duration: 14,
          lessons: 35
        },
        {
          id: 6,
          title: 'Node.js و Express',
          description: 'ساخت API‌های RESTful با Node.js و Express.',
          category: 'برنامه‌نویسی',
          level: 'متوسط',
          duration: 11,
          lessons: 26
        },
        {
          id: 7,
          title: 'مقدمه‌ای بر امنیت سایبری',
          description: 'اصول بنیادی امنیت سایبری و محافظت از تهدیدات.',
          category: 'امنیت',
          level: 'مبتدی',
          duration: 9,
          lessons: 22
        },
        {
          id: 8,
          title: 'Kubernetes برای متخصصین',
          description: 'مدیریت و استقرار اپلیکیشن‌ها با Kubernetes.',
          category: 'DevOps',
          level: 'پیشرفته',
          duration: 18,
          lessons: 40
        },
        {
          id: 9,
          title: 'اصول React',
          description: 'آموزش React و ساخت رابط‌های کاربری مدرن.',
          category: 'وب',
          level: 'متوسط',
          duration: 13,
          lessons: 32
        },
        {
          id: 10,
          title: 'Network Security',
          description: 'امنیت شبکه و محافظت از حملات شبکه‌ای.',
          category: 'امنیت',
          level: 'پیشرفته',
          duration: 16,
          lessons: 36
        },
        {
          id: 11,
          title: 'Python برای هکرها',
          description: 'استفاده از Python برای امنیت و تست نفوذ.',
          category: 'برنامه‌نویسی',
          level: 'پیشرفته',
          duration: 14,
          lessons: 33
        },
        {
          id: 12,
          title: 'CI/CD Pipeline',
          description: 'ساخت خط لوله بهینه برای تهیه و استقرار.',
          category: 'DevOps',
          level: 'متوسط',
          duration: 10,
          lessons: 24
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
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.tutorials-page h2 {
  font-size: 42px;
  margin-bottom: 40px;
  text-align: center;
}

.filter-tabs {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 40px;
  flex-wrap: wrap;
}

.tab {
  padding: 10px 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  background: transparent;
  color: white;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
  font-weight: 500;
}

.tab:hover {
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
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 25px;
}

.tutorial-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 25px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  position: relative;
}

.tutorial-card:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.level {
  position: absolute;
  top: 15px;
  right: 15px;
  padding: 5px 12px;
  border-radius: 5px;
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

.tutorial-card h3 {
  font-size: 20px;
  margin-bottom: 12px;
  margin-top: 30px;
  line-height: 1.4;
}

.description {
  font-size: 14px;
  opacity: 0.8;
  margin-bottom: 20px;
  flex-grow: 1;
  line-height: 1.6;
}

.meta {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  font-size: 13px;
  opacity: 0.7;
}

.start-btn {
  padding: 12px 24px;
  background: white;
  color: #667eea;
  border: none;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 14px;
}

.start-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .tutorials-page h2 {
    font-size: 28px;
  }
  
  .filter-tabs {
    justify-content: flex-start;
    overflow-x: auto;
  }
  
  .tutorials-grid {
    grid-template-columns: 1fr;
  }
}
</style>
