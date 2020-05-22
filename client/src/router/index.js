import Vue from 'vue';
import VueRouter from 'vue-router';
import Properties from '../components/Properties.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Properties',
    component: Properties,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
