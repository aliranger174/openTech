<template>
  <div class="home-page">
    <div class="container">
      <section class="hero">
        <h2>خوش آمدید به TechHub</h2>
        <p>بزرگترین منبع اطلاعات درباره تکنولوژی، لینوکس و امنیت سایبری</p>
        <div class="hero-buttons">
          <router-link to="/news" class="btn btn-primary">اخبار تازه</router-link>
          <router-link to="/tutorials" class="btn btn-secondary">شروع یادگیری</router-link>
        </div>
      </section>

      <section class="categories">
        <div class="category-card">
          <div class="icon">📰</div>
          <h3>اخبار تکنولوژی</h3>
          <p>آخرین اخبار دنیای فناوری و توسعه نرم‌افزار</p>
          <router-link to="/news" class="link">مشاهده</router-link>
        </div>

        <div class="category-card">
          <div class="icon">🎓</div>
          <h3>آموزش‌ها</h3>
          <p>آموزش‌های عملی درباره لینوکس، برنامه‌نویسی و امنیت</p>
          <router-link to="/tutorials" class="link">مشاهده</router-link>
        </div>

        <div class="category-card">
          <div class="icon">📚</div>
          <h3>کتاب‌های فنی</h3>
          <p>معرفی بهترین کتاب‌ها برای تعمیق دانش تکنولوژی</p>
          <router-link to="/books" class="link">مشاهده</router-link>
        </div>

        <div class="category-card">
          <div class="icon">🔒</div>
          <h3>امنیت سایبری</h3>
          <p>مقالات و آموزش‌های تخصصی درباره امنیت دیجیتال</p>
          <router-link to="/news" class="link">مشاهده</router-link>
        </div>
      </section>

      <section class="featured">
        <h3>محتوای برگزیده</h3>
        <div class="featured-items">
          <div class="featured-item">
            <div class="tag">جدید</div>
            <h4>راهنمای کامل لینوکس برای مبتدیان</h4>
            <p>یاد بگیرید چگونه لینوکس را نصب و استفاده کنید...</p>
          </div>
          <div class="featured-item">
            <div class="tag">ترند</div>
            <h4>هوش مصنوعی در توسعه نرم‌افزار</h4>
            <p>نقش هوش مصنوعی در آینده برنامه‌نویسی...</p>
          </div>
          <div class="featured-item">
            <div class="tag">مهم</div>
            <h4>10 نکته برای ایمن‌تر شدن آنلاین</h4>
            <p>نکات عملی برای محافظت از حریم خصوصی و امنیت...</p>
          </div>
        </div>
      </section>
    </div>
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
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.hero {
  text-align: center;
  margin-bottom: 80px;
  animation: fadeIn 0.8s ease-in;
}

.hero h2 {
  font-size: 48px;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.hero p {
  font-size: 20px;
  margin-bottom: 40px;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 12px 30px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
  display: inline-block;
  font-size: 16px;
}

.btn-primary {
  background: #fff;
  color: #667eea;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.btn-secondary {
  background: transparent;
  color: white;
  border: 2px solid white;
}

.btn-secondary:hover {
  background: white;
  color: #667eea;
}

.categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 30px;
  margin-bottom: 80px;
}

.category-card {
  background: rgba(255, 255, 255, 0.1);
  padding: 30px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  transition: all 0.3s;
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
}

.category-card:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.category-card .icon {
  font-size: 48px;
  margin-bottom: 15px;
}

.category-card h3 {
  margin-bottom: 10px;
  font-size: 20px;
}

.category-card p {
  font-size: 14px;
  opacity: 0.8;
  margin-bottom: 20px;
}

.link {
  color: white;
  text-decoration: none;
  font-weight: 600;
  border-bottom: 2px solid white;
  transition: all 0.3s;
  display: inline-block;
}

.link:hover {
  opacity: 0.8;
}

.featured {
  background: rgba(255, 255, 255, 0.95);
  padding: 50px;
  border-radius: 10px;
  color: #333;
}

.featured h3 {
  font-size: 32px;
  margin-bottom: 30px;
  color: #667eea;
}

.featured-items {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.featured-item {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  position: relative;
  transition: all 0.3s;
}

.featured-item:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
}

.featured-item .tag {
  position: absolute;
  top: -10px;
  right: 15px;
  background: #667eea;
  color: white;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
}

.featured-item h4 {
  margin-top: 10px;
  margin-bottom: 10px;
  color: #667eea;
}

.featured-item p {
  font-size: 14px;
  color: #666;
}

@keyframes fadeIn {
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
    font-size: 32px;
  }
  
  .featured {
    padding: 20px;
  }
}
</style>
