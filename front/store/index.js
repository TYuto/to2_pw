import axios from 'axios'

export const state = () => ({
  authUser: null,
  locales: ['en', 'ja'],
  locale: 'ja'
})

export const mutations = {
  SET_USER (state, user) {
    state.authUser = user
  },
  SET_LANG (state, locale) {
    if (state.locales.includes(locale)) {
      state.locale = locale
    }
  }
}

export const actions = {
  async logout ({ commit }) {
    await axios.get('/api/logout')
    commit('SET_USER', null)
  }
}
