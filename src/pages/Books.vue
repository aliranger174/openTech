<template>
  <div class="books-page">
    <div class="container">
      <h2>کتاب‌های تخصصی</h2>

      <div class="books-grid">
        <div 
          v-for="book in books" 
          :key="book.id"
          class="book-card"
        >
          <div class="book-cover">
            <div class="cover-icon">{{ book.icon }}</div>
            <div class="publisher">{{ book.publisher }}</div>
          </div>
          <h3>{{ book.title }}</h3>
          <p class="author">نویسنده: {{ book.author }}</p>
          <p class="description">{{ book.description }}</p>
          <div class="book-info">
            <span class="pages">📄 {{ book.pages }} صفحه</span>
            <span class="year">📅 {{ book.year }}</span>
          </div>
          <div class="rating">
            <span class="stars">⭐ {{ book.rating }}/5</span>
          </div>
          <button class="download-btn">مشاهده بیشتر</button>
        </div>
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
          description: 'راهنمای جامع خط فرمان لینوکس و Bash scripting.',
          publisher: 'No Starch Press',
          pages: 480,
          year: 2019,
          rating: 4.8,
          icon: '🐧'
        },
        {
          id: 2,
          title: 'Linux: The Complete Reference',
          author: 'Richard Petersen',
          description: 'مرجع کامل سیستم عامل لینوکس با پوشش جامع.',
          publisher: 'McGraw-Hill',
          pages: 1152,
          year: 2020,
          rating: 4.6,
          icon: '🐧'
        },
        {
          id: 3,
          title: 'The Web Application Hacker\'s Handbook',
          author: 'Stuttard, Pinto',
          description: 'نقاط ضعف و روش‌های هک برنامه‌های وب.',
          publisher: 'Wiley',
          pages: 896,
          year: 2021,
          rating: 4.9,
          icon: '🔓'
        },
        {
          id: 4,
          title: 'Cryptography Engineering',
          author: 'Schneier, Ferguson, Kohno',
          description: 'اصول و عملیات رمزنگاری و امنیت داده.',
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
          description: 'آموزش جامع زبان برنامه‌نویسی Python.',
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
          description: 'راهنمای عملی Kubernetes برای مدیریت Container‌ها.',
          publisher: 'Manning',
          pages: 664,
          year: 2020,
          rating: 4.7,
          icon: '⛵'
        },
        {
          id: 7,
          title: 'The Pragmatic Programmer',
          author: 'Hunt, Thomas',
          description: 'نکات عملی و بهترین تمرین‌های برنامه‌نویسی.',
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
          description: 'مسلط شدن بر سیستم کنترل نسخه Git.',
          publisher: 'Manning',
          pages: 432,
          year: 2020,
          rating: 4.6,
          icon: '🔧'
        },
        {
          id: 9,
          title: 'Metasploit: The Penetration Tester\'s Guide',
          author: 'Kennedy, O\'Neil, others',
          description: 'استفاده از Metasploit برای تست نفوذ و امنیت.',
          publisher: 'No Starch Press',
          pages: 384,
          year: 2021,
          rating: 4.8,
          icon: '⚔️'
        },
        {
          id: 10,
          title: 'Docker Deep Dive',
          author: 'Nigel Poulton',
          description: 'درک عمیق Docker و Container technology.',
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
          description: 'ساخت و طراحی سرویس‌های وب RESTful.',
          publisher: "O'Reilly",
          pages: 448,
          year: 2019,
          rating: 4.6,
          icon: '🌐'
        },
        {
          id: 12,
          title: 'The DevOps Handbook',
          author: 'Gene Kim, others',
          description: 'روش‌های بهترین DevOps و استقرار مداوم.',
          publisher: 'IT Revolution',
          pages: 512,
          year: 2020,
          rating: 4.8,
          icon: '⚙️'
        }
      ]
    }
  }
}
</script>

<style scoped>
.books-page {
  color: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.books-page h2 {
  font-size: 42px;
  margin-bottom: 40px;
  text-align: center;
}

.books-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.book-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 20px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
}

.book-card:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.book-cover {
  background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.1) 100%);
  height: 200px;
  border-radius: 8px;
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.cover-icon {
  font-size: 64px;
  margin-bottom: 10px;
  z-index: 1;
}

.publisher {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.5);
  padding: 8px;
  font-size: 12px;
  text-align: center;
}

.book-card h3 {
  font-size: 18px;
  margin-bottom: 8px;
  line-height: 1.4;
}

.author {
  font-size: 13px;
  opacity: 0.7;
  margin-bottom: 10px;
  color: #b3d9ff;
}

.description {
  font-size: 13px;
  opacity: 0.8;
  margin-bottom: 15px;
  flex-grow: 1;
  line-height: 1.5;
}

.book-info {
  display: flex;
  gap: 15px;
  margin-bottom: 12px;
  font-size: 12px;
  opacity: 0.7;
}

.rating {
  margin-bottom: 15px;
}

.stars {
  font-size: 13px;
  color: #ffd700;
}

.download-btn {
  padding: 10px 20px;
  background: white;
  color: #667eea;
  border: none;
  border-radius: 5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 13px;
}

.download-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .books-page h2 {
    font-size: 28px;
  }
  
  .books-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}
</style>
