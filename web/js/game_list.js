function generate_list_elem(list_item, game_name) {
    let game_container = document.createElement("div");
    let title = document.createElement("p");
    let start_btn = document.createElement("button");
    let detail_btn = document.createElement("button");

    title.innerHTML = game_name;
    start_btn.innerHTML = "Start";
    detail_btn.innerHTML = "Detail";

    game_container.setAttribute("class", "game_container");
    game_container.setAttribute("id", "game_container_" + game_name);

    title.setAttribute("class", "game_list_title");
    title.setAttribute("id", "game_list_title_" + game_name);

    start_btn.setAttribute("class", "start_btn");
    start_btn.setAttribute("id", "start_btn_" + game_name);
    start_btn.setAttribute("onclick", "eel.start_game('" + game_name + "')");

    detail_btn.setAttribute("class", "detail_btn");
    detail_btn.setAttribute("id", "detail_btn_title_" + game_name);
    detail_btn.setAttribute("onclick", "detail_func()");

    game_container.appendChild(title);
    game_container.appendChild(start_btn);
    game_container.appendChild(detail_btn);

    list_item.appendChild(game_container);
    return list_item;
}

function generate_list(ordered_list, game_list) {

    for(let i=0; i<game_list.length; i++) {
        let item = document.createElement("li");
        item = generate_list_elem(item, game_list[i]);
        ordered_list.appendChild(item);
    }
}
