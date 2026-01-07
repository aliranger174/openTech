<template>
  <div class="news-page">
    <div class="container">
      <h2>اخبار تکنولوژی</h2>
      <div class="search-bar">
        <input 
          v-model="searchQuery" 
          type="text" 
          placeholder="جستجو در اخبار..."
          @input="filterNews"
        >
      </div>

      <div class="news-grid">
        <article 
          v-for="article in filteredNews" 
          :key="article.id"
          class="news-card"
        >
          <div class="news-header">
            <span class="category" :style="{ background: getCategoryColor(article.category) }">
              {{ article.category }}
            </span>
            <span class="date">{{ article.date }}</span>
          </div>
          <h3>{{ article.title }}</h3>
          <p class="description">{{ article.description }}</p>
          <div class="news-footer">
            <span class="read-time">⏱️ {{ article.readTime }} دقیقه</span>
            <a href="#" class="read-more">ادامه مطلب →</a>
          </div>
        </article>
      </div>

      <div v-if="filteredNews.length === 0" class="no-results">
        نتیجه‌ای یافت نشد
      </div>
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
          date: '۶ ژانویه ۲۰۲۶',
          readTime: 5
        },
        {
          id: 2,
          title: 'OpenAI چت‌جی‌پی‌تی نسخه جدید معرفی کرد',
          description: 'نسخه جدید مدل هوش مصنوعی با قابلیت‌های بهتر برای برنامه‌نویسی.',
          category: 'هوش مصنوعی',
          date: '۵ ژانویه ۲۰۲۶',
          readTime: 4
        },
        {
          id: 3,
          title: 'آسیب‌پذیری جدید در وب‌سرورهای محبوب',
          description: 'محققان امنیتی یک آسیب‌پذیری صفر روزه در نرم‌افزارهای وب کشف کردند.',
          category: 'امنیت',
          date: '۴ ژانویه ۲۰۲۶',
          readTime: 6
        },
        {
          id: 4,
          title: 'Docker 24.0 منتشر شد',
          description: 'نسخه جدید Docker با بهبودهای قابل توجهی در عملکرد و ایمنی.',
          category: 'DevOps',
          date: '۳ ژانویه ۲۰۲۶',
          readTime: 5
        },
        {
          id: 5,
          title: 'Python 3.12 رسانه‌ای شد',
          description: 'جدیدترین نسخه Python با بهبودهای سرعت و قابلیت استفاده.',
          category: 'برنامه‌نویسی',
          date: '۲ ژانویه ۲۰۲۶',
          readTime: 7
        },
        {
          id: 6,
          title: 'رونمایی از CPU جدید اینتل',
          description: 'اینتل پردازنده‌های نسل جدید با معماری بهتر و مصرف انرژی کمتر معرفی کرد.',
          category: 'سخت‌افزار',
          date: '۱ ژانویه ۲۰۲۶',
          readTime: 5
        },
        {
          id: 7,
          title: 'Vue.js 4.0 در راه است',
          description: 'تیم Vue.js نقشه راه نسخه ۴ را منتشر کرد با تغییرات بنیادی.',
          category: 'برنامه‌نویسی',
          date: '۳۱ دسامبر ۲۰۲۵',
          readTime: 6
        },
        {
          id: 8,
          title: 'حملات سایبری بر شرکت‌های بزرگ',
          description: 'بررسی تازه‌ترین روش‌های حملات سایبری و راه‌های مقابله.',
          category: 'امنیت',
          date: '۳۰ دسامبر ۲۰۲۵',
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
    filterNews() {
      // Filtering is handled by computed property
    },
    getCategoryColor(category) {
      const colors = {
        'لینوکس': '#e74c3c',
        'هوش مصنوعی': '#3498db',
        'امنیت': '#e67e22',
        'DevOps': '#9b59b6',
        'برنامه‌نویسی': '#27ae60',
        'سخت‌افزار': '#34495e'
      }
      return colors[category] || '#667eea'
    }
  }
}
</script>

<style scoped>
.news-page {
  color: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.news-page h2 {
  font-size: 42px;
  margin-bottom: 30px;
  text-align: center;
}

.search-bar {
  margin-bottom: 40px;
}

.search-bar input {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  display: block;
  padding: 15px 20px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  background: rgba(255, 255, 255, 0.9);
  transition: all 0.3s;
}

.search-bar input:focus {
  outline: none;
  background: white;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.news-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 25px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
}

.news-card:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.news-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
  flex-wrap: wrap;
  gap: 10px;
}

.category {
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  color: white;
}

.date {
  font-size: 12px;
  opacity: 0.7;
}

.news-card h3 {
  font-size: 20px;
  margin-bottom: 12px;
  line-height: 1.4;
}

.description {
  font-size: 14px;
  opacity: 0.8;
  margin-bottom: 15px;
  flex-grow: 1;
  line-height: 1.6;
}

.news-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 15px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.read-time {
  font-size: 13px;
  opacity: 0.7;
}

.read-more {
  color: white;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
}

.read-more:hover {
  opacity: 0.7;
}

.no-results {
  text-align: center;
  font-size: 18px;
  opacity: 0.7;
  padding: 40px;
}

@media (max-width: 768px) {
  .news-page h2 {
    font-size: 28px;
  }
  
  .news-grid {
    grid-template-columns: 1fr;
  }
}
</style>
