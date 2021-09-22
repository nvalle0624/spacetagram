// from : https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

const handleLike = async (event) => {
  const imageURL = event.currentTarget.id;
  console.log("button and js work!");
  console.log(event.currentTarget.id);
  if (!event.currentTarget.className.includes(" favorite")) {
    event.currentTarget.className += " favorite";
    fetch("http://localhost:8000/api/favorites/", {
      method: "POST",
      body: JSON.stringify({
        image_url: await imageURL,
        id: await imageURL.replace(/[\/https:\.]/g, ""),
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    }).then((results) => results.json());
  } else {
    event.currentTarget.className = event.currentTarget.className.replace(" favorite", "");
    let url = "http://localhost:8000/api/delete" + "/" + imageURL.replace(/[\/https:\.]/g, "");
    fetch(url, {
      method: "DELETE",
      body: JSON.stringify({
        image_url: await imageURL,
        id: await imageURL,
      }),
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    }).then((results) => results.json());
    console.log("deleted");
  }
};

window.onclick = function (event) {
  let vid = document.getElementById("myVideo");
  vid.muted = false;
};

function handleScroll() {
  vid = document.getElementById("myVideo");
  vid.muted = false;
  const slideVar = setInterval(() => {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "smooth",
    });
    window.clearInterval(slideVar);
  }, 350);
}
