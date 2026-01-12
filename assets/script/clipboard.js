document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".copy-btn").forEach((button) => {
        button.addEventListener("click", () => {
            const codeBlock = button.closest(".card").querySelector(".code");
            const text = Array.from(codeBlock.querySelectorAll("pre"))
                .map((pre) => pre.textContent)
                .join("\n");

            navigator.clipboard.writeText(text).then(() => {
                button.textContent = "已複製";
                setTimeout(() => (button.textContent = "複製"), 1500);
            });
        });
    });
});
