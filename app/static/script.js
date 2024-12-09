document.getElementById("generate-btn").addEventListener("click", async (event) => {
    event.preventDefault();  // Prevent the form from submitting and reloading the page

    const imageUrl = document.getElementById("image-url").value;
    const output = document.getElementById("response-output");

    if (!imageUrl) {
        output.textContent = "Please enter a valid image URL.";
        return;
    }

    try {
        // Send URL to the backend
        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ image_url: imageUrl }),
        });

        // Handle the response
        const data = await response.text();
        if (response.ok) {
            output.style.display = "block";
            output.textContent = data; // Display the pattern
        } else {
            output.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        output.textContent = "An error occurred. Please try again.";
    }
});
