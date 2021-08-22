if (window.location.pathname === "/") {
    // api requests
    // get all todos
    function getAllTodos() {
        $.ajax({
            url: "/api",
            method: "GET",
            success: response => {
                const data = response.data.todos;
                const todo_list = document.querySelector("#todo-list");
                data.map(item => {
                    todo_list.innerHTML += `
                        <p><small>${item.name}</small></p>
                        <p>${item.text}</p>
                    `
                })
            },
            error: err => {
                console.log(err);
            }
        })
    }

    function postCreateTodo() {
        $.ajax({
            url: "/api",
            method: "POST",
            data: {
                "text": $("#text").val(),
                "name": $("#name").val()
            },
            success: response => {
                console.log(response);
            },
            error: err => {
                console.log(err);
            }
            
        })
    }
    
    getAllTodos();
    
    $("#add-todo").on("submit", () => {
        postCreateTodo();
    });
}
