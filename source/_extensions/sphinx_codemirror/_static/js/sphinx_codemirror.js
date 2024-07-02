document.addEventListener("DOMContentLoaded", function() {
  
  
      document.querySelectorAll('.codemirror-container').forEach((container) => {
          const textarea = container.querySelector('textarea');
          const editor = CodeMirror.fromTextArea(textarea, {
              lineNumbers: true,
              mode: "python",
              theme: "default",
              indentUnit: 4  // Specify the number of spaces for indentation
          });
          container.editor = editor;
      });
  
});
