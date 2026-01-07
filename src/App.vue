<template>
  <div class="app">
    <div v-if="loading" class="progress-bar" :style="{ width: progress + '%' }"></div>
    
    <header class="header">
      <div class="header-content">
        <div class="logo">
          <h1>TechHub</h1>
        </div>
        <button class="menu-toggle" @click="mobileMenuOpen = !mobileMenuOpen">
          <span></span>
          <span></span>
          <span></span>
        </button>
        <nav class="nav" :class="{ active: mobileMenuOpen }">
          <router-link to="/" class="nav-link" @click="mobileMenuOpen = false">صفحه اصلی</router-link>
          <router-link to="/news" class="nav-link" @click="mobileMenuOpen = false">اخبار</router-link>
          <router-link to="/tutorials" class="nav-link" @click="mobileMenuOpen = false">آموزش‌ها</router-link>
          <router-link to="/books" class="nav-link" @click="mobileMenuOpen = false">کتاب‌ها</router-link>
        </nav>
      </div>
    </header>
    
    <main class="main">
      <router-view></router-view>
    </main>
    
    <footer class="footer">
      <p>© 2026 TechHub</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      loading: true,
      progress: 0,
      mobileMenuOpen: false
    }
  },
  watch: {
    '$route'() {
      this.startProgress()
    }
  },
  mounted() {
    this.startProgress()
  },
  methods: {
    startProgress() {
      this.loading = true
      this.progress = 10
      
      const interval = setInterval(() => {
        if (this.progress < 90) {
          this.progress += Math.random() * 30
        }
      }, 200)
      
      setTimeout(() => {
        this.progress = 100
        clearInterval(interval)
        setTimeout(() => {
          this.loading = false
        }, 300)
      }, 1000)
    }
  }
}
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
  transition: width 0.3s ease;
  z-index: 200;
  box-shadow: 0 0 10px rgba(102, 126, 234, 0.8);
}

.header {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.08);
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  color: #667eea;
  font-size: 22px;
  margin: 0;
  padding: 12px 0;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
  gap: 6px;
}

.menu-toggle span {
  width: 24px;
  height: 2.5px;
  background: #667eea;
  border-radius: 2px;
  transition: all 0.3s;
}

.nav {
  display: flex;
  gap: 25px;
  align-items: center;
}

.nav-link {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  transition: all 0.3s;
  font-size: 14px;
  padding: 8px 0;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #667eea;
  transition: width 0.3s;
}

.nav-link:hover::after,
.nav-link.router-link-active::after {
  width: 100%;
}

.main {
  flex: 1;
  padding: 30px 16px;
}

.footer {
  background: rgba(0, 0, 0, 0.85);
  color: white;
  text-align: center;
  padding: 24px 16px;
  margin-top: auto;
  font-size: 13px;
  letter-spacing: 0.5px;
}

.footer p {
  margin: 0;
}

@media (max-width: 768px) {
  .menu-toggle {
    display: flex;
  }
  
  .nav {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    flex-direction: column;
    background: white;
    padding: 16px;
    gap: 12px;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s;
    border-bottom: 1px solid #f0f0f0;
  }
  
  .nav.active {
    max-height: 400px;
  }
  
  .nav-link {
    padding: 10px 0;
    font-size: 15px;
  }
  
  .logo h1 {
    font-size: 18px;
  }
  
  .main {
    padding: 20px 12px;
  }
  
  .footer {
    padding: 16px 12px;
  }
}

@media (max-width: 480px) {
  .logo h1 {
    font-size: 16px;
  }
  
  .main {
    padding: 16px 10px;
  }
}
</style>
