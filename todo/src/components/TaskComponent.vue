<script setup lang="ts">
import { ExclamationCircleIcon, XMarkIcon, PaperClipIcon, CheckIcon,  PencilSquareIcon } from "@heroicons/vue/24/solid";
import { ref } from "vue";
import type TaskInterface from "../types/Task";

let isEdit = ref(false);
let removeScreen = ref(false);

const props = defineProps<{
  task: TaskInterface;
}>();

const emit = defineEmits<{
  (e: "removeTask", id: number): void;
  (e: "editTask", task: TaskInterface): void;
}>();

let taskLocal:TaskInterface = { ...props.task };

const removeTask = (id: number) => {
  emit("removeTask", id);
};
const editTask = (taskLocal: TaskInterface) => {
  emit("editTask", taskLocal);
  isEdit.value = !isEdit.value;
};
const taskCheck = (taskLocal: TaskInterface) => {
  taskLocal.isChecked = !taskLocal.isChecked;
  emit("editTask", taskLocal);
};
</script>

<template>
  <transition
    enter-active-class="transition transform duration-500 ease-in-out"
    enter-from-class="scale-y-0 opacity-0 translate-y-1/2"
    enter-to-class="scale-y-full opacity-100 translate-y-0"
    leave-active-class="transition transform duration-500 ease-in-out"
    leave-from-class="scale-y-full opacity-100 translate-y-0"
    leave-to-class="scale-y-0 opacity-0 translate-y-1/2"
  >
    <div class="flex flex-col gap-2 mb-3" v-if="isEdit">
      <input
        v-model="taskLocal.title"
        type="text"
        class="p-1 text-center rounded-md"
      />
      <select v-model="taskLocal.state" class="text-center p-1">
        <option value="important">Important</option>
        <option value="dontForget">Don't Forget</option>
      </select>
      <button
        @click.prevent="editTask(taskLocal)"
        class="p-2 bg-blue-400 rounded-xl"
      >
        edit
      </button>
    </div>
  </transition>
  <div
    class="flex justify-between mb-2 shadow-2xl gap-2 bg-gradient-to-r from-white to-slate-300 rounded-xl items-center p-3 pt-6 relative"
  >
    <div class="absolute -ml-2 top-0 flex left-0 right-0 justify-between">
      <PaperClipIcon class="w-9 -mt-3" />      
      <p class="underline decoration-solid break-all text-rose-400 text-xs">
        Created At:
        {{new Date(taskLocal.created_at as Date).toLocaleDateString() }}
      </p>
      <div class="flex gap-2">
        <PencilSquareIcon
          @click.prevent="isEdit = !isEdit"
          class="w-5 text-black hover:text-blue-400 cursor-pointer"
          stroke="rose-600"
        />
        <XMarkIcon
          @click.prevent="removeScreen = !removeScreen"
          class="w-6 hover:text-red-400 cursor-pointer"
        />
      </div>
    </div>
    <ExclamationCircleIcon
      class="w-6 h-6 text-center"
      :class="[taskLocal.state === 'important' ? 'text-red-600' : 'text-green-600']"
    />
    <p
      class="transition-all flex-1 duration-1000 ease-in-out break-all text-center text-xl"
      :class="[
        taskLocal.isChecked ? ['line-through', 'text-slate-400'] : 'text-slate-700',
      ]"
    >
      {{ taskLocal.title }}
    </p>
    <CheckIcon
      v-model="taskLocal.isChecked"
      @click.prevent="taskCheck(taskLocal)"
      class="w-8 h-8 text-center transition-all rounded-full hover:bg-green-300 duration-500 ease-in-out cursor-pointer"
      :class="[taskLocal.isChecked ? 'text-green-600' : 'text-gray-400']"
    />
  </div>
  <transition
    enter-active-class="transform transition duration-1000 ease-in-out"
    enter-from-class="-translate-y-1/2 opacity-0 scale-y-0"
    enter-to-class="translate-y-0 opacity-100 scale-y-100"
    leave-active-class="transform transition duration-500 ease-in-out"
    leave-from-class="translate-y-0 opacity-100 scale-y-100"
    leave-to-class="-translate-y-1/2 opacity-00 scale-y-0"
  >
    <div
      class="flex flex-col p-1 bg-white rounded-xl items-center"
      v-if="removeScreen"
    >
      <h1 class="text-rose-400 text-center">Remove Task</h1>
      <p class="text-slate-400">Task will be removed! Are you sure?</p>
      <div class="flex gap-2">
        <button
          @click.prevent="removeScreen = !removeScreen"
          class="p-1 px-4 rounded-xl bg-red-600"
        >
          No
        </button>
        <button
          @click.prevent="removeTask(taskLocal.id as any as number)"
          class="p-1 px-4 rounded-xl bg-green-600"
        >
          Yes
        </button>
      </div>
    </div>
  </transition>
</template>
