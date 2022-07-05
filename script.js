    alert("Warning:It will require internet.");
    setInterval(() => {
        
        let a;
        a = new date();
        date = a.toLocaleDateString()
        document.getElementById ('date') .innerhtml = date
    }, 100);
    function changeColor(id)
    {
      document.getElementById(id).style.color = "blue";
    }
