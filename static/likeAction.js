const handleLike = (event) => {
  console.log("button and js work!");
  console.log(event.currentTarget.id);
  if (!event.currentTarget.className.includes(" liked")) {
    event.currentTarget.className += " liked";
  } else {
    event.currentTarget.className = event.currentTarget.className.replace(" liked", "");
  }
};
