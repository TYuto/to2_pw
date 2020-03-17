require('dotenv').config()
export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: '世界一短い短縮URL作成ツール | shortest-URL.com',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
      '@/plugins/utils',
      '@/plugins/axios',
      '@/plugins/font-awesome',
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    'bootstrap-vue/nuxt',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
    [
      'nuxt-i18n',
      {
        strategy: 'prefix_and_default',
        seo: true,
        locales: [
          { code: 'ja', iso: 'ja_JP', file: 'ja.json' },
          { code: 'en', iso: 'en-US', file: 'en.json' },
        ],
        defaultLocale: 'ja',
        vueI18n: {
          fallbackLocale: 'en',
        },
        vueI18nLoader: true,
        lazy: true,
        langDir: 'locales/',
      },
    ],
    '@nuxtjs/axios',
    '@nuxtjs/proxy',
    '@nuxtjs/recaptcha'
  ],

  bootstrapVue: {
    icons: true // Install the IconsPlugin (in addition to BootStrapVue plugin
  },
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    baseURL: "http://localhost:3000",
    browserBaseURL: "https://shortest-url.com",
  },

  proxy: [
    ['/auth/**', { target: 'http://python:8000', changeOrigin: false}],
    ['/api/**', { target: 'http://python:8000/', changeOrigin: false}],
    [[
      '/*',
      '!/_nuxt/**',
      '!/',
      '!/p/**',
      '!/release/**',
      '!/en/**',
      '!/en',
      '!/404**',
      '!/favicon.png'
    ], {target: 'http://python:8000/', changeOrigin: false}],
  ],

  recaptcha: {
    hideBadge: false, // Hide badge element (v3)
    siteKey: process.env.RECAPTCHA_SITEKEY ,    // Site key for requests
    version: 3     // Version
  },

  router: {
  },
  /*
  /*
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend (config, ctx) {
      config.resolve.alias["vue"] = "vue/dist/vue.common";
    }
  }
}
