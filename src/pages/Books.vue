<template>
  <div class="books-page">
    <h2>کتاب‌ها</h2>

    <div class="books-grid">
      <div 
        v-for="book in books" 
        :key="book.id"
        class="book-card"
        @click="goToDetail(book.id)"
        style="cursor: pointer;"
      >
        <div class="book-cover">
          <div class="cover-icon">{{ book.icon }}</div>
        </div>
        <h3>{{ book.title }}</h3>
        <p class="author">{{ book.author }}</p>
        <p class="description">{{ book.description }}</p>
        <div class="info">
          <span>{{ book.pages }} صفحه</span>
          <span>{{ book.year }}</span>
        </div>
        <div class="rating">⭐ {{ book.rating }}</div>
        <button class="btn" @click.prevent>بیشتر</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Books',
  data() {
    return {
      books: [
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
        },
        {
          id: 7,
          title: 'Pragmatic Programmer',
          author: 'Hunt, Thomas',
          description: 'نکات عملی برنامه‌نویسی.',
          publisher: 'Addison-Wesley',
          pages: 352,
          year: 2019,
          rating: 4.8,
          icon: '👨‍💻'
        },
        {
          id: 8,
          title: 'Git in Action',
          author: 'Mike McQuaid',
          description: 'مسلط شدن بر سیستم Git.',
          publisher: 'Manning',
          pages: 432,
          year: 2020,
          rating: 4.6,
          icon: '🔧'
        },
        {
          id: 9,
          title: 'Metasploit Penetration',
          author: 'Kennedy, O\'Neil',
          description: 'استفاده از Metasploit.',
          publisher: 'No Starch',
          pages: 384,
          year: 2021,
          rating: 4.8,
          icon: '⚔️'
        },
        {
          id: 10,
          title: 'Docker Deep Dive',
          author: 'Nigel Poulton',
          description: 'درک عمیق Docker.',
          publisher: 'Nigel Poulton',
          pages: 552,
          year: 2022,
          rating: 4.7,
          icon: '📦'
        },
        {
          id: 11,
          title: 'RESTful Web Services',
          author: 'Leonard Richardson',
          description: 'طراحی سرویس‌های RESTful.',
          publisher: "O'Reilly",
          pages: 448,
          year: 2019,
          rating: 4.6,
          icon: '🌐'
        },
        {
          id: 12,
          title: 'DevOps Handbook',
          author: 'Gene Kim',
          description: 'روش‌های بهترین DevOps.',
          publisher: 'IT Revolution',
          pages: 512,
          year: 2020,
          rating: 4.8,
          icon: '⚙️'
        }
      ]
    }
  },
  methods: {
    goToDetail(id) {
      this.$router.push(`/books/${id}`)
    }
  }
}
</script>

<style scoped>
.books-page {
  color: white;
  max-width: 1200px;
  margin: 0 auto;
}

.books-page h2 {
  font-size: 36px;
  margin-bottom: 32px;
  text-align: center;
  font-weight: 700;
  background: linear-gradient(135deg, #a78bfa 0%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}

.book-card {
  background: rgba(124, 58, 237, 0.1);
  padding: 16px;
  border-radius: 8px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(124, 58, 237, 0.3);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
}

.book-card:active {
  background: rgba(124, 58, 237, 0.15);
  transform: translateY(-3px);
}

.book-cover {
  background: linear-gradient(135deg, rgba(124,58,237,0.2) 0%, rgba(6,182,212,0.2) 100%);
  height: 140px;
  border-radius: 6px;
  margin-bottom: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid rgba(124, 58, 237, 0.3);
}

.cover-icon {
  font-size: 48px;
}

.book-card h3 {
  font-size: 14px;
  margin-bottom: 6px;
  line-height: 1.3;
  font-weight: 600;
  color: #c4b5fd;
}

.author {
  font-size: 11px;
  opacity: 0.6;
  margin-bottom: 8px;
  color: #a5f3fc;
}

.description {
  font-size: 12px;
  opacity: 0.75;
  margin-bottom: 10px;
  flex-grow: 1;
  line-height: 1.4;
  color: #cbd5e1;
}

.info {
  display: flex;
  gap: 12px;
  margin-bottom: 8px;
  font-size: 11px;
  opacity: 0.6;
  color: #cbd5e1;
}

.rating {
  font-size: 12px;
  color: #fbbf24;
  margin-bottom: 10px;
}

.btn {
  padding: 8px 12px;
  background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
  color: white;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 12px;
}

.btn:active {
  transform: scale(0.95);
  box-shadow: 0 2px 8px rgba(124, 58, 237, 0.3);
}

@media (max-width: 768px) {
  .books-page h2 {
    font-size: 24px;
  }
  
  .books-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 12px;
  }
}

@media (max-width: 480px) {
  .books-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .book-card {
    padding: 12px;
  }
  
  .book-cover {
    height: 100px;
  }
  
  .cover-icon {
    font-size: 36px;
  }
}
</style>
