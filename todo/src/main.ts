import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import "../src/assets/css/style.css";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:8000/api/todo/todo";

const app = createApp(App);
app.config.errorHandler = (err) => {
  console.log(err);
};

app.use(createPinia());
app.use(router);

app.mount("#app");
