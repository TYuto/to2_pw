import axios from 'axios'

export const state = () => ({
  authUser: null
})

export const mutations = {
  SET_USER: function (state, user) {
    state.authUser = user
  },
}

export const actions = {
  async logout({ commit }) {
    await axios.get('/api/logout')
    commit('SET_USER', null)
  }
}