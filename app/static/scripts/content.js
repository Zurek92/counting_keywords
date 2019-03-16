document.querySelector('form button').addEventListener('click', () => {
    let userUrl = document.querySelector('form input[name="url"]').value
    let caseSensitive = document.querySelector('form div.checkbox input[name="case_sensitive"]').checked
    let user_json = JSON.stringify({'url': userUrl, 'case_sensitive': caseSensitive});
    fetch('/keywords', {
        method: 'post',
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        },
        body: user_json
    })
    .then(resp => resp.json())
    .then(resp => {
        let errorMessage = document.querySelector('form div.errorMessage');
        if (resp['succes']) {
            errorMessage.innerHTML = ''
            const tableParts = [];
            for (let elem in resp['words']) {
                tableParts.push(`<tr><td>${elem}</td><td>${resp['words'][elem]}</td></tr>`);
            }
            let preparedTable = `
            <tr><th>keyword</th><th>counts</th></tr>
            ${tableParts.join('')}
            `
            document.querySelector('table').innerHTML = preparedTable;
        } else {
            errorMessage.innerHTML = resp['message']
        }

    })
})
