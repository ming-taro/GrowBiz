<template>
  <section ref="editor" style="height: 500px"></section>
</template>

<script>
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';
import Quill from 'quill';
import { onMounted, ref, watch, onUnmounted } from 'vue';

const defaultOptions = {
  theme: 'snow',
  modules: {
    toolbar: [
      ['bold', 'italic', 'underline', 'strike'],
      ['blockquote', 'code-block'],
      [{ header: 1 }, { header: 2 }],
      [{ list: 'ordered' }, { list: 'bullet' }],
      [{ script: 'sub' }, { script: 'super' }],
      [{ indent: '-1' }, { indent: '+1' }],
      [{ direction: 'rtl' }],
      [{ size: ['small', false, 'large', 'huge'] }],
      [{ header: [1, 2, 3, 4, 5, 6, false] }],
      [{ color: [] }, { background: [] }],
      [{ font: [] }],
      [{ align: [] }],
      ['clean'],
      ['link', 'image', 'video']
    ]
  },
  placeholder: '내용을 입력하세요',
  readOnly: false
};

export default {
  name: 'quill-editor',
  props: {
    modelValue: { // v-model을 위한 prop
      type: String,
      default: ''
    },
    disabled: {
      type: Boolean,
      default: false
    },
    options: {
      type: Object,
      required: false,
      default: () => ({})
    }
  },
  emits: ['update:modelValue', 'blur', 'focus'],
  setup(props, context) {
    const editor = ref(null);
    const quill = ref(null);

    const initialize = () => {
      if (editor.value) {
        const editorOption = { ...defaultOptions, ...props.options };
        editorOption.readOnly = props.disabled;
        quill.value = new Quill(editor.value, editorOption);

        // 초기 값 설정
        quill.value.root.innerHTML = props.modelValue;

        // 포커스/블러 이벤트
        quill.value.on('selection-change', range => {
          if (range) {
            context.emit('focus');
          } else {
            context.emit('blur');
          }
        });

        // 내용 변경 이벤트
        quill.value.on('text-change', () => {
          const html = quill.value.root.innerHTML;
          context.emit('update:modelValue', html); // 변경된 내용을 부모에게 전달
        });

        // 비활성화 상태 반영
        if (props.disabled) {
          quill.value.enable(false);
        }
      }
    };

    // 부모에서 disabled prop이 변경될 때 에디터 상태 업데이트
    watch(() => props.disabled, (newVal) => {
      if (quill.value) {
        quill.value.enable(!newVal);
      }
    });

    // 부모에서 modelValue prop이 변경될 때 에디터 내용 업데이트
    watch(() => props.modelValue, (newVal) => {
      if (quill.value && newVal !== quill.value.root.innerHTML) {
        quill.value.root.innerHTML = newVal; // 외부에서 modelValue가 변경될 때 에디터 내용도 변경
      }
    });

    onMounted(() => {
      initialize();
    });

    onUnmounted(() => {
      quill.value = null;
    });

    return { editor };
  }
};
</script>

<style scoped>
</style>
