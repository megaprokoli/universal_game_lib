function generate_detail_tab(game_data) {
    var gamename = game_data["gamename"];

    let tab_div = document.createElement("div");
    let title = document.createElement("p");
    let meta_list = document.createElement("ul");
    let game_name_item = document.createElement("li");
    let appid = document.createElement("li");
    let size = document.createElement("li");
    let launcher = document.createElement("li");
    let close_btn = document.createElement("button");

    tab_div.setAttribute("class", "detail_tab");
    tab_div.setAttribute("id", "detail_tab_" + gamename);

    title.setAttribute("class", "title_detail_tab");

    meta_list.setAttribute("class", "metadata_list");

    game_name_item.setAttribute("class", "metadata_list_item");
    game_name_item.setAttribute("id", "gamename_" + gamename);

    appid.setAttribute("class", "metadata_list_item");
    appid.setAttribute("id", "appid_" + gamename);

    size.setAttribute("class", "metadata_list_item");
    size.setAttribute("id", "size_" + gamename);

    launcher.setAttribute("class", "metadata_list_item");
    launcher.setAttribute("id", "launcher_" + gamename);

    close_btn.setAttribute("class", "list_item_close");
    close_btn.setAttribute("id", "close_" + gamename);
    close_btn.setAttribute("onclick", "detail_tab.hide_details('game_container_" + gamename + "', 'detail_tab_" + gamename + "')");

    game_name_item.innerHTML = "Game: " + gamename;
    appid.innerHTML = "AppID: " + game_data["appid"];
    size.innerHTML = "Size: " + game_data["extra"]["SizeOnDisk"];
    launcher.innerHTML = "Launcher: " + game_data["launcher"];

    title.innerHTML = "Details:"
    close_btn.innerHTML = "X";

    meta_list.appendChild(game_name_item);
    meta_list.appendChild(appid);
    meta_list.appendChild(size);
    meta_list.appendChild(launcher);

    tab_div.appendChild(close_btn);
    tab_div.appendChild(title);
    tab_div.appendChild(meta_list);

    return tab_div;
}

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
    detail_btn.setAttribute("onclick", "detail_tab.show_details('game_container_" + game_name + "', '" + game_name + "')");

    game_container.appendChild(title);
    game_container.appendChild(start_btn);
    game_container.appendChild(detail_btn);

    list_item.appendChild(game_container);
    return list_item;
}

function generate_list(ordered_list, game_list) {

    console.log(game_list);

    for(let i=0; i<game_list.length; i++) {
        let item = document.createElement("li");

        item.setAttribute("class", "game_list_item");
        item = generate_list_elem(item, game_list[i]);
        ordered_list.appendChild(item);
    }
}

function search_game(input_id) {
    var search = document.getElementById(input_id).value;

    if(search == "") {  //if no search str entered list all games
        load_games();
    } else {
        load_games(search);
    }
}

function load_games(filter=null) {
    console.log(filter);
    get_games(filter).then(JSON.parse).then( function(r){
        //clear list before creating a new one
        var list = document.getElementById("game_list");

        while(list.firstChild) {
            list.removeChild(list.firstChild);
        }
        console.log("Gamelist cleared");

        //generate the list
        generate_list(list, r["data"]);
        console.log("Gamelist generated");
    });
}


async function get_games(filter) {
    return await eel.get_game_names(filter)();    //TODO sort alphabet
}

async function get_game_data(game_name) {
    return await eel.get_game_data(game_name)();
}

var detail_tab = {
    open: false,

    show_details: function(game_cont_id, game_name) {
        if(!this.open){
            this.open = true;

            get_game_data(game_name).then(JSON.parse).then(function(result){

                let cont = document.getElementById(game_cont_id);
                cont.appendChild(generate_detail_tab(result));
            });
        }
    },

    hide_details: function(game_cont_id, tab_id) {
        document.getElementById(game_cont_id).removeChild(document.getElementById(tab_id));
        this.open = false;
    }
}
