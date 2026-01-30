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
        @click="goToDetail(tutorial.id)"
        style="cursor: pointer;"
      >
        <img :src="getImageForCategory(tutorial.category)" :alt="tutorial.title" class="tutorial-image">
        <div class="level" :class="tutorial.level.toLowerCase()">
          {{ tutorial.level }}
        </div>
        <h3>{{ tutorial.title }}</h3>
        <p>{{ tutorial.description }}</p>
        <div class="meta">
          <span>{{ tutorial.duration }} ساعت</span>
          <span>{{ tutorial.lessons }} درس</span>
        </div>
        <button class="start-btn" @click.prevent>شروع</button>
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
  },
  methods: {
    getImageForCategory(category) {
      const images = {
        'لینوکس': '/images/category-linux.svg',
        'امنیت': '/images/category-security.svg',
        'برنامه‌نویسی': '/images/category-programming.svg',
        'DevOps': '/images/category-devops.svg'
      }
      return images[category] || '/images/category-tutorials.svg'
    },
    goToDetail(id) {
      this.$router.push(`/tutorials/${id}`)
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
  background: linear-gradient(135deg, #a78bfa 0%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
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
  border: 2px solid rgba(124, 58, 237, 0.4);
  background: transparent;
  color: #e2e8f0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 13px;
  font-weight: 500;
}

.tab:active {
  border-color: #7c3aed;
  background: rgba(124, 58, 237, 0.1);
}

.tab.active {
  background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
  color: white;
  border-color: transparent;
}

.tutorials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}

.tutorial-card {
  background: rgba(124, 58, 237, 0.1);
  padding: 20px;
  border-radius: 8px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(124, 58, 237, 0.3);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.tutorial-card:active {
  background: rgba(124, 58, 237, 0.15);
  transform: translateY(-3px);
}

.tutorial-image {
  width: calc(100% + 40px);
  margin-left: -20px;
  margin-right: -20px;
  margin-top: -20px;
  margin-bottom: 15px;
  height: 130px;
  object-fit: cover;
  border-radius: 0;
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
  background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
}

.level.متوسط {
  background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
}

.level.پیشرفته {
  background: linear-gradient(135deg, #ef4444 0%, #f97316 100%);
}

.tutorial-card h3 {
  font-size: 15px;
  margin-bottom: 8px;
  margin-top: 24px;
  line-height: 1.4;
  font-weight: 600;
  color: #c4b5fd;
}

.tutorial-card p {
  font-size: 12px;
  opacity: 0.75;
  margin-bottom: 12px;
  flex-grow: 1;
  line-height: 1.5;
  color: #cbd5e1;
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
  background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 12px;
}

.start-btn:active {
  transform: scale(0.95);
  box-shadow: 0 2px 8px rgba(124, 58, 237, 0.3);
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
