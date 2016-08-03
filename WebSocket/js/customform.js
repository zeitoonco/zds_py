/**
 * Created by Pedram2 on 7/30/2016.
 */

$(document).ready(function () {

    $('#addCategory').jsonForm({
        schema: {
            title: {
                type: 'string',
                title: 'Title',
                required: true
            },
            type: {
                type: 'number',
                title: 'Type',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.newCategory', {
                    userid: 1,
                    title: values.title,
                    type: parseInt(values.type)

                });
            }
        }
    });
    $('#modifyCategory').jsonForm({
        schema: {
            id: {
                type: 'number',
                title: 'ID',
                required: true
            },
            title: {
                type: 'string',
                title: 'Title',
                required: true
            },
            type: {
                type: 'number',
                title: 'Type',
                required: true

            },
            category: {
                type: 'number',
                title: 'Category',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.modifyCategory', {
                    id: parseInt(values.id),
                    title: values.title,
                    type: parseInt(values.type),
                    category: values.category
                });
            }
        }
    });
    $('#removeCategory').jsonForm({
        schema: {
            id: {
                type: 'number',
                title: 'ID',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.removeCategory', {
                    id: parseInt(values.id)
                });
            }
        }
    });


    $('#newTopic').jsonForm({
        schema: {
            title: {
                type: 'string',
                title: 'Title',
                required: true
            },
            parent: {
                type: 'number',
                title: 'Parent',
                required: true

            },
            category: {
                type: 'number',
                title: 'Category',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.newTopic', {
                    userid: 1,
                    title: values.title,
                    parent: parseInt(values.parent),
                    category: values.category
                });
            }
        }
    });
    $('#modifyTopic').jsonForm({
        schema: {
            id: {
                type: 'number',
                title: 'ID',
                required: true
            },
            title: {
                type: 'string',
                title: 'Title',
                required: true
            },
            parent: {
                type: 'number',
                title: 'Parent',
                required: true

            },
            category: {
                type: 'number',
                title: 'Category',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.modifyTopic', {
                    id: values.id,
                    title: values.title,
                    parent: parseInt(values.parent),
                    category: values.category
                });
            }
        }
    });
    $('#removeTopic').jsonForm({
        schema: {
            id: {
                type: 'number',
                title: 'ID',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.removeTopic', {
                    id: parseInt(values.id)
                });
            }
        }
    });


    $('#newAccount').jsonForm({
        schema: {
            parent: {
                type: 'number',
                title: 'Parent',
                required: true
            },
            type: {
                type: 'number',
                title: 'Type',
                required: true

            },
            code: {
                type: 'string',
                title: 'Code',
                required: true
            },
            TitleID: {
                type: 'number',
                title: 'TitleID',
                required: true
            },
            Title2: {
                type: 'string',
                title: 'Title2',
                required: true
            },
            IsActive: {
                type: 'boolean',
                title: 'IsActive',
                required: true
            },
            CashFlowCategory: {
                type: 'number',
                title: 'CashFlowCategory',
                required: true
            },
            OpeningBalance: {
                type: 'number',
                title: 'OpeningBalance',
                required: true
            },

            BalanceType: {
                type: 'number',
                title: 'BalanceType',
                required: true,
                enum: [1, 3, 3]
            },
            HasBalanceTypeCheck: {
                type: 'boolean',
                title: 'HasBalanceTypeCheck',
                required: true
            },
            HasDL: {
                type: 'boolean',
                title: 'HasDL',
                required: true
            },
            HasCurrency: {
                type: 'boolean',
                title: 'HasCurrency',
                required: true
            },
            HasTracking: {
                type: 'boolean',
                title: 'HasTracking',
                required: true
            }


        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.newCategory', {
                    title: values.title,
                    parent: parseInt(values.parent),
                    category: values.category
                });
            }
        }
    });
    $('#modifyAccount').jsonForm({
        schema: {
            id: {
                type: 'number',
                title: 'ID',
                required: true
            },
            title: {
                type: 'string',
                title: 'Title',
                required: true
            },
            parent: {
                type: 'number',
                title: 'Parent',
                required: true

            },
            category: {
                type: 'number',
                title: 'Category',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.modifyCategory', {
                    id: values.id,
                    title: values.title,
                    parent: parseInt(values.parent),
                    category: values.category
                });
            }
        }
    });
    $('#removeAccount').jsonForm({
        schema: {
            id: {
                type: 'number',
                title: 'ID',
                required: true

            }
        },
        onSubmit: function (errors, values) {
            if (errors) {
                toastr.error("خطا");

            }
            else {
                sendCMD('AccountingRelay.removeCategory', {
                    id: parseInt(values.id)
                });
            }
        }
    });


});

var Socket;
var sessionid = -1;
var skiplogin = 0;

var CBProcs = {
    "userman.login": cbLogin,

    "_core.getListOfServices": "List of registered Services",
    "_core.getServiceInfo": "Service Info",

    "userman.registerPermission": "New Permission ID",
    "userman.listUsers": "List of Users",
    "userman.listUsersByGroup": "List of Users",
    "userman.addUser": "UserID",
    "userman.getUserInfo": "User Info",

    "userman.listPermissions": "List of Permissions",
    "userman.listUserPermissions": "List of User Permissions",
    "userman.checkPermission": "Permissions State",
    "userman.checkPermissionByName": "Permissions State",

    "userman.registerUsergroup": "New UserGroup ID",
    "userman.listUsergroups": "List of UserGroups",
    "AccountingRelay.getConfig": "getConfig",
    "AccountingRelay.setConfig": "setConfig",
    "AccountingRelay.newCategory": "newCategory",
    "userman.listUsergroupPermissions": "List of Usergroup Permissions"
};

$(document).ready(function () {
    $("#connect").click(function () {
        Socket = new WebSocket("ws://" + $("#wshost").val() + ":" + $("#wsport").val());
        Socket.onmessage = dataReceived;
        Socket.onclose = function () {
            $('#statusColor').css('color', 'red');
            toastr.error("ارتباط قطع شد");
        };
        Socket.onopen = function () {
            $('#statusColor').css('color', 'green');
            toastr.success("اتصال برقرار شد");
        };
        Socket.onerror = function (er) {
            $('#statusColor').css('color', 'red');
            toastr.error("ارتباط قطع شد");
            console.error("WS Error : " + er);
        };
    });
    $("#disconnect").click(function () {
        Socket.close();
    });

    $("#sendCMD").click(function () {
        sendCMD($("#icmd").val(), JSON.parse($("#ijson").val()));
    });
    $("#login").click(function () {
        if (sessionid == -1) {
            var msg = {
                type: "call",
                node: "userman.login",
                id: "1234568",
                data: {username: $("#iUser").val(), password: $("#iPass").val()}
            }
        } else {
            var msg = {
                type: "call",
                node: "userman.logout",
                id: "1234568",
                data: {value: sessionid}
            }
            $("#login").attr('value', 'Login');
            $("#sessionid").html("");
            sessionid = -1;
        }
        Socket.send(JSON.stringify(msg));
    })

});

function dataReceived(ev) {
    console.log("WSR: " + ev.data);
    var packet = JSON.parse(ev.data);

    if ((packet.type == "callback")) {
        /*if (packet.node == "_core.getListOfServices") {
         view = "List of Services:<table border=\"1\"><tr><th>Name</th><th>Version</th><th>State</th></tr>";
         var states = ["unknown", "not Installed", "Installing", "Installed", "Enable"];
         for (var s in packet.data.extensions) {
         ss = packet.data.extensions[s];
         view += "<tr><td>" + ss.name + "</td><td>" + ss.version + "</td><td>" + states[ss.state] + "</td></tr>";
         }
         view += "</table>";
         $("#data").html(view);
         }else
         if (packet.node == "userman.listUsers") {
         view = "List of Services:<table border=\"1\"><tr><th>ID</th><th>UserName</th><th>Name</th><th>Ban</th><th>BanReason</th></tr>";
         for (var s in packet.data.userList) {
         ss = packet.data.userList[s];
         view += "<tr><td>" + ss.userID + "</td><td>" + ss.username + "</td><td>" + ss.name + "</td><td>" + ss.banned + "</td><td>" + ss.banReason + "</td></tr>";
         }
         view += "</table>";
         $("#data").html(view);
         }else
         if (packet.node == "userman.getUserInfo") {
         ss=packet.data;
         $("#data").html("User " + ss.userID + "#" + ss.username + " (" + ss.name + "). ban:" + ss.banned + " r " + ss.banReason + ".");
         }else
         if (packet.node == "userman.listPermissions") {
         view = "List of Services:<table border=\"1\"><tr><th>ID</th><th>Parent</th><th>Name</th><th>title</th><th>desc</th></tr>";
         for (var s in packet.data.listPermissions) {
         ss = packet.data.listPermissions[s];
         view += "<tr><td>" + ss.permissionID + "</td><td>" + ss.parentID + "</td><td>" + ss.name + "</td><td>" + ss.title + "</td><td>" + ss.description + "</td></tr>";
         }
         view += "</table>";
         $("#data").html(view);
         }else
         if (packet.node == "") {
         view = "List of Services:<table border=\"1\"><tr><th>ID</th><th>State</th></tr>";
         for (var s in packet.data.listPermissions) {
         ss = packet.data.listPermissions[s];
         view += "<tr><td>" + ss.id + "</td><td>" + ss.state + "</td></tr>";
         }
         view += "</table>";
         $("#data").html(view);
         }*/
        CBProcessor(packet.node, packet.data);
    } else if (packet.type == "error") {
        $("#data").html("ERROR on '" + packet.node + "' {" + packet.id + "} : " + packet.data);
    }
}

function cbLogin(data) {
    if (data.result == "ok") {
        sessionid = data.sessionID;
        $("#sessionid").html("ok:" + sessionid);
        $("#login").attr('value', 'Logout');
    } else {
        $("#sessionid").html("Failed:" + data.description);
        sessionid = -1;
        $("#login").attr('value', 'Login');
    }
}

function CBProcessor(node, data) {//data is structure for sure. its childs can be anything
    var v = CBProcs[node];
    switch (typeof(v)) {
        case "function":
            v(data);
            break;
        case "string":
            var view = "<h1>" + v + " :</h1>" + CBPDrawer(data);
            $("#data").html(view);
            break;
        case "undefined":
            console.log("CBP Err type '" + typeof(v) + "' for " + node);
            break;
    }
}

function CBPDrawer(data) {
    var view = "";
    if (typeof(data) == "object") {
        if (Array.isArray(data)) {
            if (data.length == 0)
                view = "[]";
            else if (typeof(data[0]) == "object" && !Array.isArray(data[0])) {//table
                view = "<table class='tblST'><tr>";
                for (var s in data[0])
                    view += "<th>" + s + "</th>";
                view += "</tr><tr>";
                for (var i = 0; i < data.length; i++) {
                    for (var s in data[i]) {
                        view += "<td>" + CBPDrawer(data[i][s]) + "</td>";
                    }
                    view += "</tr><tr>";
                }
                view += "</tr></table>";
            } else {
                view = "<table class='tblST'>";
                for (var i = 0; i < data.length; i++) {
                    view += "<tr><td>" + CBPDrawer(data[i]) + "</td></tr>";
                }
                view += "</table>";
            }
        } else {//struct
            if (structLength(data) < 3) {
                view = "<div class='pad10'>";
                for (var s in data)
                    view = "<h3>" + s + ":</h3>" + CBPDrawer(data[s]);
                view += "</div>";
            } else {
                view = "<table class='tblST pad10'>";
                for (var s in data) {
                    view += "<tr><th>" + s + "</th><td>" + CBPDrawer(data[s]) + "</td></tr>";
                }
                view += "</table>";
            }
        }
    } else {
        view = data.toString();
    }
    return view;
}

function sendCMD(inode, idata) {
    if (skiplogin != 110 && sessionid == -1) {
        toastr.error("ابتدا وارد شوید!");
        return;
    }
    var ss = "";
    if (!idata)
        ss = (JSON.stringify({
            type: 'call',
            node: inode,
            id: Math.round(Math.random() * 1000000000).toString()
        }));
    else
        ss = (JSON.stringify({
            type: 'call',
            node: inode,
            id: Math.round(Math.random() * 1000000000).toString(),
            data: idata
        }));
    console.log("SenD:" + ss);
    Socket.send(ss);
}

function structLength(st) {
    var c = 0;
    for (var s in st) {
        c++;
    }
    return c;
}
