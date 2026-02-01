<template>
  <div class="home-page">
    <section class="hero">
      <h2>خوش آمدید</h2>
      <p>بزرگترین منبع اطلاعات تکنولوژی</p>
      <div class="hero-buttons">
        <router-link to="/news" class="btn btn-primary">اخبار</router-link>
        <router-link to="/tutorials" class="btn btn-secondary">یادگیری</router-link>
      </div>
    </section>

    <section class="categories">
      <router-link to="/news" class="category-card">
        <img src="/images/news.svg" alt="اخبار" class="card-image">
        <h3>اخبار</h3>
        <p>آخرین اخبار فناوری</p>
        <span class="link">→</span>
      </router-link>

      <router-link to="/tutorials" class="category-card">
        <img src="/images/tutorials.svg" alt="آموزش" class="card-image">
        <h3>آموزش</h3>
        <p>دوره‌های تخصصی</p>
        <span class="link">→</span>
      </router-link>

      <router-link to="/books" class="category-card">
        <img src="/images/books.svg" alt="کتاب‌ها" class="card-image">
        <h3>کتاب‌ها</h3>
        <p>منابع فنی معروف</p>
        <span class="link">→</span>
      </router-link>

      <router-link to="/news" class="category-card">
        <img src="/images/news.svg" alt="امنیت" class="card-image">
        <h3>امنیت</h3>
        <p>مقالات امنیتی</p>
        <span class="link">→</span>
      </router-link>

      <router-link to="/projects" class="category-card">
        <img src="/images/projects.svg" alt="پروژه‌ها" class="card-image">
        <h3>پروژه‌ها</h3>
        <p>نمونه‌های کاری</p>
        <span class="link">→</span>
      </router-link>
    </section>

    <section class="featured">
      <h3>برگزیده</h3>
      <div class="featured-items">
        <div class="featured-item">
          <div class="tag">جدید</div>
          <h4>راهنمای لینوکس</h4>
          <p>یادگیری لینوکس برای مبتدیان</p>
        </div>
        <div class="featured-item">
          <div class="tag">ترند</div>
          <h4>هوش مصنوعی</h4>
          <p>نقش AI در برنامه‌نویسی</p>
        </div>
        <div class="featured-item">
          <div class="tag">مهم</div>
          <h4>امنیت آنلاین</h4>
          <p>نکات محافظت حریم خصوصی</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home-page {
  color: white;
  max-width: 1200px;
  margin: 0 auto;
}

.hero {
  text-align: center;
  margin-bottom: 50px;
  animation: slideUp 0.6s ease-out;
}

.hero h2 {
  font-size: 42px;
  margin-bottom: 12px;
  font-weight: 700;
  letter-spacing: -1px;
  text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  background: linear-gradient(135deg, #a78bfa 0%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero p {
  font-size: 18px;
  margin-bottom: 32px;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 12px 24px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  display: inline-block;
  font-size: 14px;
  min-height: 44px;
  display: flex;
  align-items: center;
}

.btn-primary {
  background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
  color: white;
}

.btn-primary:active {
  transform: scale(0.98);
  box-shadow: 0 0 20px rgba(124, 58, 237, 0.4);
}

.btn-secondary {
  background: transparent;
  color: white;
  border: 2px solid rgba(124, 58, 237, 0.6);
}

.btn-secondary:active {
  background: rgba(124, 58, 237, 0.1);
  border-color: rgba(124, 58, 237, 1);
}

.categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 16px;
  margin-bottom: 50px;
}

.category-card {
  background: rgba(124, 58, 237, 0.1);
  padding: 20px;
  border-radius: 8px;
  backdrop-filter: blur(10px);
  transition: all 0.3s;
  border: 1px solid rgba(124, 58, 237, 0.3);
  text-align: center;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.category-card:active {
  background: rgba(124, 58, 237, 0.2);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(124, 58, 237, 0.2);
}

.category-card .card-image {
  width: 100%;
  height: 120px;
  object-fit: cover;
  border-radius: 6px;
  margin-bottom: 12px;
}

.category-card .icon {
  font-size: 36px;
  margin-bottom: 12px;
}

.category-card h3 {
  margin-bottom: 6px;
  font-size: 16px;
}

.category-card p {
  font-size: 12px;
  opacity: 0.75;
  margin-bottom: 12px;
}

.link {
  color: white;
  text-decoration: none;
  font-weight: 600;
  display: inline-block;
  opacity: 0.8;
  transition: all 0.3s;
  pointer-events: none;
}

.link:active {
  opacity: 1;
}

.featured {
  background: rgba(15, 23, 42, 0.4);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(124, 58, 237, 0.3);
  padding: 32px 20px;
  border-radius: 8px;
  color: #e2e8f0;
}

.featured h3 {
  font-size: 24px;
  margin-bottom: 24px;
  color: #a78bfa;
  font-weight: 700;
}

.featured-items {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 16px;
}

.featured-item {
  background: rgba(124, 58, 237, 0.1);
  padding: 16px;
  border-radius: 6px;
  position: relative;
  transition: all 0.3s;
  border: 1px solid rgba(124, 58, 237, 0.3);
}

.featured-item:active {
  box-shadow: 0 3px 10px rgba(124, 58, 237, 0.2);
  transform: translateY(-2px);
  background: rgba(124, 58, 237, 0.15);
}

.featured-item .tag {
  position: absolute;
  top: -8px;
  right: 12px;
  background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
  color: white;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 11px;
  font-weight: 600;
}

.featured-item h4 {
  margin-top: 8px;
  margin-bottom: 8px;
  color: #a78bfa;
  font-size: 14px;
}

.featured-item p {
  font-size: 12px;
  color: #cbd5e1;
  line-height: 1.4;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .hero h2 {
    font-size: 28px;
  }
  
  .hero p {
    font-size: 15px;
  }
  
  .hero-buttons {
    gap: 12px;
  }
  
  .categories {
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
  }
  
  .featured {
    padding: 24px 16px;
  }
  
  .featured-items {
    gap: 12px;
  }
}

@media (max-width: 480px) {
  .hero h2 {
    font-size: 22px;
    margin-bottom: 10px;
  }
  
  .hero p {
    font-size: 13px;
    margin-bottom: 18px;
  }
  
  .hero-buttons {
    gap: 10px;
    flex-direction: column;
  }
  
  .btn {
    padding: 12px 18px;
    font-size: 13px;
    width: 100%;
    justify-content: center;
  }
  
  .categories {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 30px;
  }
  
  .category-card {
    padding: 14px;
  }
  
  .category-card .card-image {
    height: 100px;
    margin-bottom: 8px;
  }
  
  .category-card h3 {
    font-size: 14px;
    margin-bottom: 4px;
  }
  
  .category-card p {
    font-size: 11px;
  }
  
  .featured {
    padding: 18px 12px;
  }
  
  .featured h3 {
    font-size: 20px;
    margin-bottom: 16px;
  }
  
  .featured-items {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  
  .featured-item {
    padding: 14px;
  }
  
  .featured-item h4 {
    font-size: 13px;
    margin-bottom: 6px;
  }
  
  .featured-item p {
    font-size: 11px;
  }
}
</style>
