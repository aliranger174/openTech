<template>
  <div class="news-page">
    <h2>اخبار</h2>
    <div class="search-bar">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="جستجو..."
      >
    </div>

    <div class="news-grid">
      <article 
        v-for="article in filteredNews" 
        :key="article.id"
        class="news-card"
        @click="goToDetail(article.id)"
        style="cursor: pointer;"
      >
        <img :src="getImageForCategory(article.category)" :alt="article.title" class="news-image">
        <div class="news-header">
          <span class="category" :style="{ background: getCategoryColor(article.category) }">
            {{ article.category }}
          </span>
          <span class="date">{{ article.date }}</span>
        </div>
        <h3>{{ article.title }}</h3>
        <p>{{ article.description }}</p>
        <div class="footer">
          <span class="read-time">{{ article.readTime }} دقیقه</span>
          <a href="#" class="read-more" @click.prevent>ادامه →</a>
        </div>
      </article>
    </div>

    <div v-if="filteredNews.length === 0" class="no-results">
      نتیجه‌ای یافت نشد
    </div>
  </div>
</template>

<script>
export default {
  name: 'News',
  data() {
    return {
      searchQuery: '',
      news: [
        {
          id: 1,
          title: 'لینوکس کرنل 6.5 منتشر شد',
          description: 'جدیدترین نسخه لینوکس کرنل با بهبودهای عملکردی و امنیتی منتشر شده است.',
          category: 'لینوکس',
          date: '۶ ژانویه',
          readTime: 5
        },
        {
          id: 2,
          title: 'ChatGPT نسخه جدید',
          description: 'نسخه جدید مدل هوش مصنوعی با قابلیت‌های بهتر برای برنامه‌نویسی.',
          category: 'AI',
          date: '۵ ژانویه',
          readTime: 4
        },
        {
          id: 3,
          title: 'آسیب‌پذیری جدید کشف شد',
          description: 'محققان امنیتی یک آسیب‌پذیری صفر روزه در نرم‌افزارهای وب کشف کردند.',
          category: 'امنیت',
          date: '۴ ژانویه',
          readTime: 6
        },
        {
          id: 4,
          title: 'Docker 24.0',
          description: 'نسخه جدید Docker با بهبودهای قابل توجهی در عملکرد.',
          category: 'DevOps',
          date: '۳ ژانویه',
          readTime: 5
        },
        {
          id: 5,
          title: 'Python 3.12 رسانه‌ای شد',
          description: 'جدیدترین نسخه Python با بهبودهای سرعت.',
          category: 'برنامه‌نویسی',
          date: '۲ ژانویه',
          readTime: 7
        },
        {
          id: 6,
          title: 'CPU جدید اینتل',
          description: 'اینتل پردازنده‌های نسل جدید با معماری بهتر.',
          category: 'سخت‌افزار',
          date: '۱ ژانویه',
          readTime: 5
        },
        {
          id: 7,
          title: 'Vue.js 4.0 در راه است',
          description: 'تیم Vue.js نقشه راه نسخه ۴ را منتشر کرد.',
          category: 'برنامه‌نویسی',
          date: '۳۱ دسامبر',
          readTime: 6
        },
        {
          id: 8,
          title: 'حملات سایبری',
          description: 'بررسی تازه‌ترین روش‌های حملات و راه‌های مقابله.',
          category: 'امنیت',
          date: '۳۰ دسامبر',
          readTime: 8
        }
      ]
    }
  },
  computed: {
    filteredNews() {
      return this.news.filter(article => 
        article.title.includes(this.searchQuery) || 
        article.description.includes(this.searchQuery) ||
        article.category.includes(this.searchQuery)
      )
    }
  },
  methods: {
    getCategoryColor(category) {
      const colors = {
        'لینوکس': '#e74c3c',
        'AI': '#3498db',
        'امنیت': '#e67e22',
        'DevOps': '#9b59b6',
        'برنامه‌نویسی': '#27ae60',
        'سخت‌افزار': '#34495e'
      }
      return colors[category] || '#667eea'
    },
    getImageForCategory(category) {
      const images = {
        'لینوکس': '/images/category-linux.svg',
        'AI': '/images/category-ai.svg',
        'امنیت': '/images/category-security.svg',
        'DevOps': '/images/category-devops.svg',
        'برنامه‌نویسی': '/images/category-programming.svg',
        'سخت‌افزار': '/images/category-hardware.svg'
      }
      return images[category] || '/images/news.svg'
    },
    goToDetail(id) {
      this.$router.push(`/news/${id}`)
    }
  }
}
</script>

<style scoped>
.news-page {
  color: white;
  max-width: 1200px;
  margin: 0 auto;
}

.news-page h2 {
  font-size: 36px;
  margin-bottom: 24px;
  text-align: center;
  font-weight: 700;
  background: linear-gradient(135deg, #a78bfa 0%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.search-bar {
  margin-bottom: 32px;
}

.search-bar input {
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
  display: block;
  padding: 12px 16px;
  border: none;
  border-radius: 6px;
  font-size: 14px;
  background: rgba(124, 58, 237, 0.15);
  color: #e2e8f0;
  border: 1px solid rgba(124, 58, 237, 0.4);
  transition: all 0.3s;
  min-height: 44px;
}

.search-bar input::placeholder {
  color: #94a3b8;
}

.search-bar input:focus {
  outline: none;
  background: rgba(124, 58, 237, 0.2);
  border-color: rgba(124, 58, 237, 0.7);
  box-shadow: 0 4px 12px rgba(124, 58, 237, 0.2);
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 18px;
  margin-bottom: 32px;
}

.news-card {
  background: rgba(124, 58, 237, 0.1);
  padding: 20px;
  border-radius: 8px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(124, 58, 237, 0.3);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.news-card:active {
  background: rgba(124, 58, 237, 0.15);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(124, 58, 237, 0.2);
}

.news-image {
  width: calc(100% + 40px);
  margin-left: -20px;
  margin-right: -20px;
  margin-top: -20px;
  margin-bottom: 15px;
  height: 150px;
  object-fit: cover;
  border-radius: 0;
}

.news-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  gap: 10px;
}

.category {
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  color: white;
}

.date {
  font-size: 11px;
  opacity: 0.6;
}

.news-card h3 {
  font-size: 16px;
  margin-bottom: 10px;
  line-height: 1.4;
  font-weight: 600;
  color: #c4b5fd;
}

.news-card p {
  font-size: 13px;
  opacity: 0.75;
  margin-bottom: 12px;
  flex-grow: 1;
  line-height: 1.5;
  color: #cbd5e1;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 12px;
}

.read-time {
  opacity: 0.6;
}

.read-more {
  color: white;
  text-decoration: none;
  font-weight: 600;
}

.no-results {
  text-align: center;
  font-size: 14px;
  opacity: 0.6;
  padding: 32px;
}

@media (max-width: 768px) {
  .news-page h2 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .search-bar {
    margin-bottom: 24px;
  }
  
  .search-bar input {
    max-width: 100%;
  }
  
  .news-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  
  .news-card {
    display: grid;
    grid-template-columns: 100px 1fr;
    gap: 12px;
    padding: 12px;
  }
  
  .news-image {
    width: 100px;
    height: 100px;
    margin: 0;
    grid-row: 1 / 4;
  }
  
  .news-card h3 {
    font-size: 14px;
    margin: 0;
  }
  
  .news-card p {
    font-size: 12px;
    margin: 0;
  }
}

@media (max-width: 480px) {
  .news-page h2 {
    font-size: 20px;
    margin-bottom: 16px;
  }
  
  .search-bar {
    margin-bottom: 18px;
  }
  
  .search-bar input {
    padding: 10px 12px;
    font-size: 13px;
  }
  
  .news-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }
  
  .news-card {
    padding: 12px;
  }
  
  .news-image {
    width: 80px;
    height: 80px;
  }
  
  .news-header {
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 8px;
  }
  
  .category {
    font-size: 10px;
    padding: 3px 8px;
  }
  
  .date {
    font-size: 10px;
  }
  
  .news-card h3 {
    font-size: 13px;
    margin-bottom: 6px;
  }
  
  .news-card p {
    font-size: 11px;
    margin-bottom: 8px;
  }
  
  .footer {
    font-size: 10px;
    gap: 8px;
  }
}
</style>
