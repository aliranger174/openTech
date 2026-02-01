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
          <router-link to="/projects" class="nav-link" @click="mobileMenuOpen = false">پروژه‌ها</router-link>
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
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #15213e 100%);
}

.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #7c3aed 0%, #0ddbffff 50%, #3413adff 100%);
  transition: width 0.3s ease;
  z-index: 200;
  box-shadow: 0 0 15px rgba(124, 58, 237, 0.8);
}

.header {
  background: rgba(15, 23, 42, 0.5);
  backdrop-filter: blur(30px) saturate(180%);
  -webkit-backdrop-filter: blur(30px) saturate(180%);
  border-bottom: 1px solid rgba(124, 58, 237, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.logo h1 {
  color: #7c3aed;
  font-size: 22px;
  margin: 0;
  padding: 12px 0;
  font-weight: 700;
  letter-spacing: -0.5px;
  text-shadow: 0 2px 8px rgba(124, 58, 237, 0.3);
}

.menu-toggle {
  display: none;
  flex-direction: column;
  background: rgba(255, 255, 255, 0.3);
  border: 1px solid rgba(124, 58, 237, 0.4);
  border-radius: 6px;
  cursor: pointer;
  padding: 8px;
  gap: 6px;
  transition: all 0.3s;
  backdrop-filter: blur(10px);
  min-height: 44px;
  min-width: 44px;
  flex-shrink: 0;
}

.menu-toggle:active {
  background: rgba(124, 58, 237, 0.2);
  border-color: rgba(124, 58, 237, 0.6);
}

.menu-toggle span {
  width: 24px;
  height: 2.5px;
  background: #7c3aed;
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
  color: #e2e8f0;
  font-weight: 500;
  transition: all 0.3s;
  font-size: 14px;
  padding: 12px 16px;
  position: relative;
  border-radius: 6px;
  background: rgba(124, 58, 237, 0.1);
  border: 1px solid rgba(124, 58, 237, 0.3);
  backdrop-filter: blur(10px);
  min-height: 44px;
  display: flex;
  align-items: center;
}

.nav-link:hover {
  background: rgba(124, 58, 237, 0.2);
  border-color: rgba(124, 58, 237, 0.5);
  color: #a78bfa;
}

.nav-link.router-link-active {
  background: rgba(124, 58, 237, 0.3);
  color: #c4b5fd;
  border-color: rgba(124, 58, 237, 0.6);
  backdrop-filter: blur(10px);
}

.main {
  flex: 1;
  padding: 24px 12px;
}

.footer {
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(20px);
  color: #e2e8f0;
  text-align: center;
  padding: 24px 16px;
  margin-top: auto;
  font-size: 13px;
  letter-spacing: 0.5px;
  border-top: 1px solid rgba(124, 58, 237, 0.2);
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
    background: rgba(15, 23, 42, 0.5);
    backdrop-filter: blur(30px) saturate(180%);
    -webkit-backdrop-filter: blur(30px) saturate(180%);
    border: 1px solid rgba(124, 58, 237, 0.3);
    border-top: none;
    padding: 12px;
    gap: 8px;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s, visibility 0.3s;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    visibility: hidden;
  }
  
  .nav.active {
    max-height: 500px;
    visibility: visible;
  }
  
  .nav-link {
    padding: 12px 14px;
    font-size: 14px;
    background: rgba(124, 58, 237, 0.1);
    border: 1px solid rgba(124, 58, 237, 0.3);
    border-radius: 6px;
    backdrop-filter: blur(10px);
  }
  
  .nav-link:active {
    background: rgba(124, 58, 237, 0.2);
    border-color: rgba(124, 58, 237, 0.5);
  }
  
  .logo h1 {
    font-size: 18px;
  }
  
  .main {
    padding: 18px 10px;
  }
  
  .footer {
    padding: 14px 10px;
    font-size: 12px;
  }
}

@media (max-width: 480px) {
  .logo h1 {
    font-size: 16px;
    padding: 10px 0;
  }
  
  .main {
    padding: 14px 8px;
  }
  
  .header-content {
    padding: 0 12px;
  }
}
</style>
