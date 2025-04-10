document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("fireflies");

    // Clear previous fireflies if any (prevents stacking)
    container.innerHTML = "";

    for (let i = 0; i < 40; i++) {
        const firefly = document.createElement("div");
        firefly.classList.add("firefly");

        // Set random position
        firefly.style.top = Math.random() * 100 + "vh";
        firefly.style.left = Math.random() * 100 + "vw";

        // Random horizontal movement
        firefly.style.setProperty('--randomX', Math.random());

        // Delay each firefly’s animation randomly
        firefly.style.animationDelay = Math.random() * 5 + "s";

        container.appendChild(firefly);
    }
});
