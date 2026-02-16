const url = "https://basic-fastapi-backend.onrender.com/";

(async () => {
    const res = await fetch(url);
    const data = await res.json();
    console.log(data)
})()