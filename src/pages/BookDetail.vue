<template>
  <div class="book-detail">
    <button class="back-btn" @click="goBack">← بازگشت</button>
    
    <div v-if="book" class="book-container">
      <div class="book-cover-section">
        <div class="book-cover-large">
          <div class="cover-icon">{{ book.icon }}</div>
        </div>
      </div>

      <div class="book-info">
        <h1>{{ book.title }}</h1>
        <p class="author">نویسنده: {{ book.author }}</p>
        <div class="rating">⭐ {{ book.rating }}/5</div>
        
        <div class="details">
          <div class="detail-item">
            <span class="label">ناشر:</span>
            <span>{{ book.publisher }}</span>
          </div>
          <div class="detail-item">
            <span class="label">تعداد صفحات:</span>
            <span>{{ book.pages }}</span>
          </div>
          <div class="detail-item">
            <span class="label">سال انتشار:</span>
            <span>{{ book.year }}</span>
          </div>
        </div>

        <div class="description">
          <h3>توضیحات</h3>
          <p>{{ book.description }}</p>
        </div>

        <button class="btn-download">دانلود</button>
      </div>
    </div>

    <div v-else class="not-found">
      کتاب یافت نشد
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookDetail',
  data() {
    return {
      booksData: [
        {
          id: 1,
          title: 'The Linux Command Line',
          author: 'William E. Shotts',
          description: 'راهنمای جامع خط فرمان لینوکس.',
          publisher: 'No Starch Press',
          pages: 480,
          year: 2019,
          rating: 4.8,
          icon: '🐧'
        },
        {
          id: 2,
          title: 'Linux: Complete Reference',
          author: 'Richard Petersen',
          description: 'مرجع کامل سیستم عامل لینوکس.',
          publisher: 'McGraw-Hill',
          pages: 1152,
          year: 2020,
          rating: 4.6,
          icon: '🐧'
        },
        {
          id: 3,
          title: 'Web Hacker\'s Handbook',
          author: 'Stuttard, Pinto',
          description: 'نقاط ضعف و روش‌های هک وب.',
          publisher: 'Wiley',
          pages: 896,
          year: 2021,
          rating: 4.9,
          icon: '🔓'
        },
        {
          id: 4,
          title: 'Cryptography Engineering',
          author: 'Schneier, Ferguson',
          description: 'اصول رمزنگاری و امنیت داده.',
          publisher: 'Wiley',
          pages: 432,
          year: 2019,
          rating: 4.7,
          icon: '🔐'
        },
        {
          id: 5,
          title: 'Learning Python',
          author: 'Mark Lutz',
          description: 'آموزش جامع زبان Python.',
          publisher: "O'Reilly",
          pages: 1476,
          year: 2021,
          rating: 4.8,
          icon: '🐍'
        },
        {
          id: 6,
          title: 'Kubernetes in Action',
          author: 'Marko Lukša',
          description: 'راهنمای عملی Kubernetes.',
          publisher: 'Manning',
          pages: 664,
          year: 2020,
          rating: 4.7,
          icon: '⛵'
        }
      ]
    }
  },
  computed: {
    book() {
      const id = parseInt(this.$route.params.id)
      return this.booksData.find(b => b.id === id)
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
.book-detail {
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

.book-container {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 40px;
  background: rgba(124, 58, 237, 0.1);
  padding: 40px;
  border-radius: 12px;
  border: 1px solid rgba(124, 58, 237, 0.3);
  backdrop-filter: blur(10px);
}

.book-cover-large {
  width: 100%;
  aspect-ratio: 2 / 3;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 120px;
}

.book-info h1 {
  font-size: 28px;
  margin-bottom: 12px;
  line-height: 1.4;
}

.author {
  font-size: 16px;
  opacity: 0.8;
  margin-bottom: 16px;
  color: #cbd5e1;
}

.rating {
  font-size: 20px;
  margin-bottom: 24px;
}

.details {
  margin: 24px 0;
  padding: 24px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.detail-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  font-size: 14px;
}

.label {
  font-weight: 600;
  opacity: 0.8;
}

.description {
  margin: 24px 0;
}

.description h3 {
  margin-bottom: 12px;
  font-size: 18px;
}

.description p {
  line-height: 1.6;
  opacity: 0.9;
}

.btn-download {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  color: white;
  padding: 12px 28px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-download:hover {
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
  .book-container {
    grid-template-columns: 1fr;
    padding: 24px;
  }

  .book-cover-large {
    font-size: 80px;
  }

  .book-info h1 {
    font-size: 22px;
  }
}
</style>
