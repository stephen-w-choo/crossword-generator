document.addEventListener('DOMContentLoaded', function() {
    
    document.querySelector('#generate').onclick = () => {

        let difficulty = document.querySelector('input[name="difficulty"]:checked').value;

        fetch("/generate", {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify({"difficulty": difficulty})
        }
        // note, I'm not 100% sure if the first promise returns an array
        // or it needs to be parsed as a second promise or converted
        // assume for now that it returns a 2d array that I can use
        ).then(response => response.text())
        .then(result => console.log(result))
    }
});