function fetch_script() {
    formButton.removeEventListener('click', fetch_script)
    formButton.innerHTML = 'Waiting'
    let userUrl = document.querySelector('form input[name="url"]').value;
    let caseSensitive = document.querySelector('form div.checkbox input[name="case_sensitive"]').checked;
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
        const errorMessage = document.querySelector('form div.errorMessage');
        const outputField = document.querySelector('form output');
        if (resp['succes']) {
            errorMessage.innerHTML = ''
            const tableParts = [];
            for (let elem in resp['words']) {
                tableParts.push(`<tr><td>${elem}</td><td>${resp['words'][elem]}</td></tr>`);
            }
            let preparedTable = `
            <table>
            <tr><th>keyword</th><th>counts</th></tr>
            ${tableParts.join('')}
            </table>
            `
            outputField.innerHTML = preparedTable;
        } else {
            outputField.innerHTML = '';
            errorMessage.innerHTML = resp['message'];
        }
    })
    .then(() => {
        formButton.innerHTML = 'Submit';
        formButton.addEventListener('click', fetch_script);
    })
}

const formButton = document.querySelector('form button');
formButton.addEventListener('click', fetch_script);
