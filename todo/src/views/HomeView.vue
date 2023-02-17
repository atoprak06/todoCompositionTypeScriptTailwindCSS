<script setup lang="ts">
import { EllipsisVerticalIcon, ArrowDownIcon } from "@heroicons/vue/24/solid";
import { ref, onMounted } from "vue";
import Task from "../components/TaskComponent.vue";
import axios from "axios";
import type TaskInterface from "../types/Task";

let newTask = ref<TaskInterface>({ state: "important" });

let isExpanded = ref(false);

let tasks = ref<TaskInterface[]>([]);

const removeTask = async (id: number) => {
  await axios
    .delete(`${id}`)
    .then(() => {
      tasks.value.forEach((task, index) => {
        if (task.id === id) tasks.value.splice(index, 1);
      });
    })
    .catch((error) => {
      console.log(error);
    });
};

const addTask = async () => {
  await axios
    .post("/", newTask.value)
    .then((response) => {
      tasks.value = [response.data, ...tasks.value];
      newTask.value = { state: "important" };
    })
    .catch((error) => {
      console.log(error);
    });
};

const editTask = async (editedTask: TaskInterface) => {
  await axios
    .patch(`${editedTask.id}/`, editedTask)
    .then((response) => {
      tasks.value.forEach((task, index) => {
        if (task.id === response.data.id) {
          tasks.value[index] = response.data;
        }
      });
    })
    .catch((error) => {
      console.log(error);
    });
};

onMounted(async () => {
  await axios
    .get("")
    .then((response) => {
      tasks.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>

<template>
  <div class="home flex flex-col bg-orange-200 align-center p-2">
    <div class="sticky top-0 z-10 w-full bg-orange-200 mx-auto">
      <div class="relative">
        <h1
          class="rounded-2xl border-dashed border-b-4 border-slate-800 text-4xl text-center mt-3 pb-2"
        >
          Todo List<span class="text-5xl not-italic text-slate-300"></span>
        </h1>
        <div class="absolute flex right-0 left-0 justify-end mr-3">
          <div class="relative mt-4">
            <div
              class="absolute right-0 left-0 flex flex-row justify-between -mt-5"
            >
              <EllipsisVerticalIcon class="w-6 text-slate" />
              <EllipsisVerticalIcon class="w-6 text-slate" />
            </div>
            <p class="text-sm font-bold bg-white p-2 rounded bg-black">
              Tasks: {{ tasks?.length }}
            </p>
          </div>
        </div>
      </div>
      <div class="mt-20 grid grid-cols-1 gap-2 add-task">
        <button
          @click.prevent="isExpanded = !isExpanded"
          class="bg-slate-500 flex justify-between rounded-xl text-white p-3"
        >
          <p class="flex-1">New Task</p>
          <ArrowDownIcon
            :class="isExpanded ? 'rotate-180' : 'rotate-0'"
            class="transform transition-transform duration-500 ease-in-out w-5 float-right"
          />
        </button>
        <transition
          enter-active-class="transform transition duration-500 ease-in"
          enter-from-class="-translate-y-1/2 scale-y-0 opacity-0"
          enter-to-class="translate-y-0 scale-y-100 opacity-100"
          leave-active-class="transform transition duration-300 ease-out"
          leave-from-class="translate-y-0 scale-y-100 opacity-100"
          leave-to-class="-translate-y-1/2 scale-y-0 opacity-0"
        >
          <div v-show="isExpanded" class="flex flex-col gap-2">
            <input
              type="text"
              placeholder="Enter task.."
              class="p-3 flex-1 rounded-2xl text-center"
              v-model="newTask.title"
            />
            <select v-model="newTask.state" class="text-center rounded-xl p-3">
              <option value="important">Important</option>
              <option value="dontForget">Don't Forget</option>
            </select>
            <button @click.prevent="addTask" class="p-2 rounded-xl bg-rose-600">
              Add
            </button>
          </div>
        </transition>
      </div>
    </div>
    <div class="tasks container mx-auto mt-10">
      <ul class="p-4 grid gap-2 grid-cols-1 relative">
        <TransitionGroup
          appear
          move-class="transform transition duration-500 ease-in-out"
          enter-active-class="transform transition duration-500 ease-in-out"
          enter-from-class="opacity-0 scale-x-0 translate-x-1/2"
          enter-to-class="opacity-100 scale-x-100 translate-x-0"
          leave-active-class="transform transition duration-1000 ease-in-out absolute w-full "
          leave-from-class="opacity-100 scale-x-100 translate-x-0"
          leave-to-class="opacity-0 scale-x-0 translate-x-1/2"
        >
          <li v-for="task in tasks" :key="task.id">
            <Task
              :task="task"
              @remove-task="removeTask"
              @edit-task="editTask"
            />
          </li>
        </TransitionGroup>
      </ul>
    </div>
  </div>
</template>
