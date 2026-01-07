<template>
  <div class="app">
    <header class="header">
      <div class="container">
        <div class="logo">
          <h1>🚀 TechHub</h1>
        </div>
        <nav class="nav">
          <router-link to="/" class="nav-link">صفحه اصلی</router-link>
          <router-link to="/news" class="nav-link">اخبار</router-link>
          <router-link to="/tutorials" class="nav-link">آموزش‌ها</router-link>
          <router-link to="/books" class="nav-link">کتاب‌ها</router-link>
        </nav>
      </div>
    </header>
    
    <main class="main">
      <router-view></router-view>
    </main>
    
    <footer class="footer">
      <div class="container">
        <p>© 2026 TechHub - تمام حقوق محفوظ است</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.header {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  color: #667eea;
  font-size: 28px;
  margin: 0;
  padding: 15px 0;
}

.nav {
  display: flex;
  gap: 30px;
  align-items: center;
}

.nav-link {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: color 0.3s;
  font-size: 16px;
}

.nav-link:hover,
.nav-link.router-link-active {
  color: #667eea;
  border-bottom: 2px solid #667eea;
  padding-bottom: 3px;
}

.main {
  flex: 1;
  padding: 40px 20px;
}

.footer {
  background: rgba(0, 0, 0, 0.8);
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: 40px;
}

@media (max-width: 768px) {
  .nav {
    flex-direction: column;
    gap: 10px;
  }
  
  .logo h1 {
    font-size: 20px;
  }
}
</style>
