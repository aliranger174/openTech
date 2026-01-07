<template>
  <div class="projects-page">
    <h2>پروژه‌ها</h2>

    <div class="filter-tabs">
      <button 
        v-for="category in categories"
        :key="category"
        @click="selectedCategory = category"
        :class="{ active: selectedCategory === category }"
        class="tab"
      >
        {{ category }}
      </button>
    </div>

    <div class="projects-grid">
      <div 
        v-for="project in filteredProjects" 
        :key="project.id"
        class="project-card"
      >
        <div class="project-header">
          <div class="icon">{{ project.icon }}</div>
          <div class="status" :class="project.status">{{ project.status }}</div>
        </div>
        <h3>{{ project.title }}</h3>
        <p class="description">{{ project.description }}</p>
        <div class="technologies">
          <span v-for="tech in project.technologies" :key="tech" class="tech-tag">
            {{ tech }}
          </span>
        </div>
        <div class="footer">
          <span class="date">{{ project.date }}</span>
          <a href="#" class="view-btn">مشاهده →</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Projects',
  data() {
    return {
      selectedCategory: 'همه',
      categories: ['همه', 'وب', 'موبایل', 'ابزار', 'دیگر'],
      projects: [
        {
          id: 1,
          title: 'پلتفرم اخبار تکنولوژی',
          description: 'وبسایت منابع اخبار و آموزش تکنولوژی با طراحی مدرن.',
          category: 'وب',
          icon: '📰',
          technologies: ['Vue.js', 'Vite', 'CSS3'],
          date: 'دسامبر ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 2,
          title: 'اپ یادگیری لینوکس',
          description: 'اپلیکیشن موبایل برای یادگیری دستورات لینوکس.',
          category: 'موبایل',
          icon: '🐧',
          technologies: ['React Native', 'Node.js', 'MongoDB'],
          date: 'نوامبر ۲۰۲۵',
          status: 'درحال‌توسعه'
        },
        {
          id: 3,
          title: 'ابزار تحلیل امنیت',
          description: 'ابزار خط‌فرمانی برای بررسی امنیت وبسایت‌ها.',
          category: 'ابزار',
          icon: '🔒',
          technologies: ['Python', 'Bash', 'Linux'],
          date: 'اکتبر ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 4,
          title: 'داشبورد مدیریتی',
          description: 'داشبورد مدیریتی برای نظارت بر سرورهای لینوکس.',
          category: 'وب',
          icon: '📊',
          technologies: ['Vue.js', 'Express', 'WebSocket'],
          date: 'سپتامبر ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 5,
          title: 'کتاب‌خانه کمپایلر',
          description: 'کتاب‌خانه برای ساخت و تحلیل کمپایلرهای ساده.',
          category: 'ابزار',
          icon: '⚙️',
          technologies: ['C++', 'LLVM', 'Parser'],
          date: 'آگوست ۲۰۲۵',
          status: 'درحال‌توسعه'
        },
        {
          id: 6,
          title: 'سیستم مدیریت محتوا',
          description: 'CMS سادهاما قدرتمند برای وبسایت‌های کوچک.',
          category: 'وب',
          icon: '📝',
          technologies: ['Django', 'PostgreSQL', 'Docker'],
          date: 'ژوئیه ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 7,
          title: 'اپلیکیشن قرآن',
          description: 'اپ موبایل برای خواندن و یادگیری قرآن کریم.',
          category: 'موبایل',
          icon: '📖',
          technologies: ['Flutter', 'Firebase', 'REST API'],
          date: 'ژوئن ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 8,
          title: 'چت‌بات هوش مصنوعی',
          description: 'چت‌بات مبتنی بر هوش مصنوعی برای پاسخگویی سوالات.',
          category: 'دیگر',
          icon: '🤖',
          technologies: ['Python', 'NLP', 'TensorFlow'],
          date: 'مه ۲۰۲۵',
          status: 'درحال‌توسعه'
        },
        {
          id: 9,
          title: 'نرم‌افزار VPN',
          description: 'اپلیکیشن VPN ایمن برای مرورگر.',
          category: 'ابزار',
          icon: '🔐',
          technologies: ['Node.js', 'OpenVPN', 'Electron'],
          date: 'آپریل ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 10,
          title: 'فروشگاه آنلاین',
          description: 'پلتفرم فروش آنلاین با سیستم درگاه پرداخت.',
          category: 'وب',
          icon: '🛒',
          technologies: ['React', 'Node.js', 'Stripe API'],
          date: 'مارس ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 11,
          title: 'مدیریت وظایف تیمی',
          description: 'ابزار مدیریت پروژه و وظایف برای تیم‌های توزیع‌شده.',
          category: 'وب',
          icon: '✅',
          technologies: ['Vue.js', 'Real-time', 'WebSockets'],
          date: 'فوریه ۲۰۲۵',
          status: 'فعال'
        },
        {
          id: 12,
          title: 'سنسور IoT',
          description: 'سیستم مراقبتی هوشمند با حسگرهای IoT.',
          category: 'دیگر',
          icon: '📡',
          technologies: ['Arduino', 'Python', 'MQTT'],
          date: 'ژانویه ۲۰۲۵',
          status: 'فعال'
        }
      ]
    }
  },
  computed: {
    filteredProjects() {
      if (this.selectedCategory === 'همه') {
        return this.projects
      }
      return this.projects.filter(p => p.category === this.selectedCategory)
    }
  }
}
</script>

<style scoped>
.projects-page {
  color: white;
  max-width: 1200px;
  margin: 0 auto;
}

.projects-page h2 {
  font-size: 36px;
  margin-bottom: 24px;
  text-align: center;
  font-weight: 700;
  background: linear-gradient(135deg, #a78bfa 0%, #06b6d4 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.filter-tabs {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 32px;
  flex-wrap: wrap;
}

.tab {
  padding: 8px 16px;
  border: 2px solid rgba(124, 58, 237, 0.4);
  background: transparent;
  color: #e2e8f0;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 13px;
  font-weight: 500;
}

.tab:active {
  border-color: #7c3aed;
  background: rgba(124, 58, 237, 0.1);
}

.tab.active {
  background: linear-gradient(135deg, #7c3aed 0%, #06b6d4 100%);
  color: white;
  border-color: transparent;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 16px;
}

.project-card {
  background: rgba(124, 58, 237, 0.1);
  padding: 20px;
  border-radius: 8px;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(124, 58, 237, 0.3);
  transition: all 0.3s;
  display: flex;
  flex-direction: column;
}

.project-card:active {
  background: rgba(124, 58, 237, 0.15);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(124, 58, 237, 0.2);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.icon {
  font-size: 36px;
}

.status {
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  color: white;
}

.status.فعال {
  background: linear-gradient(135deg, #10b981 0%, #06b6d4 100%);
}

.status.درحال‌توسعه {
  background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
}

.project-card h3 {
  font-size: 16px;
  margin-bottom: 8px;
  line-height: 1.4;
  font-weight: 600;
  color: #c4b5fd;
}

.description {
  font-size: 13px;
  opacity: 0.75;
  margin-bottom: 12px;
  flex-grow: 1;
  line-height: 1.5;
  color: #cbd5e1;
}

.technologies {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 12px;
}

.tech-tag {
  display: inline-block;
  padding: 4px 10px;
  background: rgba(124, 58, 237, 0.25);
  border: 1px solid rgba(124, 58, 237, 0.5);
  border-radius: 4px;
  font-size: 11px;
  color: #c4b5fd;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 12px;
  border-top: 1px solid rgba(124, 58, 237, 0.2);
  font-size: 12px;
}

.date {
  opacity: 0.6;
  color: #cbd5e1;
}

.view-btn {
  color: #a78bfa;
  text-decoration: none;
  font-weight: 600;
}

@media (max-width: 768px) {
  .projects-page h2 {
    font-size: 24px;
  }
  
  .projects-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 12px;
  }
}

@media (max-width: 480px) {
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-card {
    padding: 16px;
  }
}
</style>
