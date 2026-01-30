<template>
  <div class="news-detail">
    <button class="back-btn" @click="goBack">← بازگشت</button>
    
    <article v-if="article" class="article">
      <img :src="getImageForCategory(article.category)" :alt="article.title" class="featured-image">
      <div class="article-header">
        <h1>{{ article.title }}</h1>
        <div class="meta">
          <span class="category" :style="{ background: getCategoryColor(article.category) }">
            {{ article.category }}
          </span>
          <span class="date">{{ article.date }}</span>
          <span class="read-time">{{ article.readTime }} دقیقه خواندن</span>
        </div>
      </div>

      <div class="article-content">
        <p>{{ article.description }}</p>
        <p>{{ article.fullContent }}</p>
      </div>
    </article>

    <div v-else class="not-found">
      مقاله یافت نشد
    </div>
  </div>
</template>

<script>
export default {
  name: 'NewsDetail',
  data() {
    return {
      newsData: [
        {
          id: 1,
          title: 'لینوکس کرنل 6.5 منتشر شد',
          description: 'جدیدترین نسخه لینوکس کرنل با بهبودهای عملکردی و امنیتی منتشر شده است.',
          fullContent: 'لینوکس کرنل 6.5 با بهبودهای زیادی برای کارایی و امنیت رسانه‌ای شده است. این نسخه شامل رفع خرابی‌های متعدد و بهبود پشتیبانی از سخت‌افزار جدید است.',
          category: 'لینوکس',
          date: '۶ ژانویه',
          readTime: 5
        },
        {
          id: 2,
          title: 'ChatGPT نسخه جدید',
          description: 'نسخه جدید مدل هوش مصنوعی با قابلیت‌های بهتر برای برنامه‌نویسی.',
          fullContent: 'OpenAI نسخه جدید ChatGPT را منتشر کرد که با بهبودهای قابل‌توجهی در درک و تولید کد برنامه‌نویسی آمده است. این نسخه سرعت بهتری دارد و دقت بیشتری را فراهم می‌کند.',
          category: 'AI',
          date: '۵ ژانویه',
          readTime: 4
        },
        {
          id: 3,
          title: 'آسیب‌پذیری جدید کشف شد',
          description: 'محققان امنیتی یک آسیب‌پذیری صفر روزه در نرم‌افزارهای وب کشف کردند.',
          fullContent: 'یک تیم از محققان امنیتی یک آسیب‌پذیری جدی در کتاب‌خانه‌های وبی محبوب کشف کردند. توصیه می‌شود تمام کاربران به‌روزرسانی کنند.',
          category: 'امنیت',
          date: '۴ ژانویه',
          readTime: 6
        },
        {
          id: 4,
          title: 'Docker 24.0',
          description: 'نسخه جدید Docker با بهبودهای قابل توجهی در عملکرد.',
          fullContent: 'Docker 24.0 با بهبودهای عملکردی و نوابغ جدید برای مدیریت کانتینرها منتشر شده است. این نسخه مصرف حافظه کمتری دارد.',
          category: 'DevOps',
          date: '۳ ژانویه',
          readTime: 5
        },
        {
          id: 5,
          title: 'Python 3.12 رسانه‌ای شد',
          description: 'جدیدترین نسخه Python با بهبودهای سرعت.',
          fullContent: 'Python 3.12 با بهبودهای قابل‌توجهی در سرعت اجرا و کارایی حافظه منتشر شده است. این نسخه تا ۲۰ درصد سریع‌تر است.',
          category: 'برنامه‌نویسی',
          date: '۲ ژانویه',
          readTime: 7
        },
        {
          id: 6,
          title: 'CPU جدید اینتل',
          description: 'اینتل پردازنده‌های نسل جدید با معماری بهتر.',
          fullContent: 'اینتل پردازنده‌های جدیدی با معماری بهبودیافته و مصرف انرژی کمتر معرفی کرد.',
          category: 'سخت‌افزار',
          date: '۱ ژانویه',
          readTime: 5
        },
        {
          id: 7,
          title: 'Vue.js 4.0 در راه است',
          description: 'تیم Vue.js نقشه راه نسخه ۴ را منتشر کرد.',
          fullContent: 'تیم Vue.js نقشه راه توسعه نسخه ۴ را اعلام کرد که شامل نوابغ و بهبودهای بزرگی خواهد بود.',
          category: 'برنامه‌نویسی',
          date: '۳۱ دسامبر',
          readTime: 6
        },
        {
          id: 8,
          title: 'حملات سایبری',
          description: 'بررسی تازه‌ترین روش‌های حملات و راه‌های مقابله.',
          fullContent: 'تحقیقات نشان می‌دهد که حملات سایبری روز به روز پیچیده‌تر می‌شوند و نیاز به استراتژی‌های دفاعی بهتر است.',
          category: 'امنیت',
          date: '۳۰ دسامبر',
          readTime: 8
        }
      ]
    }
  },
  computed: {
    article() {
      const id = parseInt(this.$route.params.id)
      return this.newsData.find(n => n.id === id)
    }
  },
  methods: {
    goBack() {
      this.$router.back()
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
    }
  }
}
</script>

<style scoped>
.news-detail {
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

.article {
  background: rgba(124, 58, 237, 0.1);
  padding: 40px;
  border-radius: 12px;
  border: 1px solid rgba(124, 58, 237, 0.3);
  backdrop-filter: blur(10px);
  overflow: hidden;
}

.featured-image {
  width: calc(100% + 80px);
  margin-left: -40px;
  margin-right: -40px;
  margin-top: -40px;
  margin-bottom: 24px;
  height: 300px;
  object-fit: cover;
  border-radius: 0;
}

.article-header h1 {
  font-size: 32px;
  margin-bottom: 20px;
  line-height: 1.4;
}

.meta {
  display: flex;
  gap: 16px;
  align-items: center;
  flex-wrap: wrap;
  margin-bottom: 32px;
  padding-bottom: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.category {
  padding: 6px 14px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  color: white;
}

.date, .read-time {
  font-size: 14px;
  opacity: 0.7;
}

.article-content {
  line-height: 1.8;
  font-size: 16px;
}

.article-content p {
  margin-bottom: 16px;
  opacity: 0.9;
}

.not-found {
  text-align: center;
  padding: 40px;
  opacity: 0.6;
  font-size: 18px;
}

@media (max-width: 768px) {
  .article {
    padding: 24px;
  }

  .article-header h1 {
    font-size: 24px;
  }

  .meta {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
