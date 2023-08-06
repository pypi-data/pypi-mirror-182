"use strict";
(self["webpackChunkcodespaces_jupyterlab"] = self["webpackChunkcodespaces_jupyterlab"] || []).push([["lib_index_js"],{

/***/ "./lib/CodespaceMenu.js":
/*!******************************!*\
  !*** ./lib/CodespaceMenu.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CodespaceMenu": () => (/* binding */ CodespaceMenu)
/* harmony export */ });
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./icons */ "./lib/icons.js");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);



class CodespaceMenu extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor(jsonData) {
        super();
        this.id = '@jupyterlab-sidepanel/example';
        this.title.iconClass = "codespace-icon jp-SideBar-tabIcon";
        this.title.caption = "Codespace Panel";
        this.data = jsonData;
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement("div", { className: "jp-CodespaceInfo" },
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("header", null, "GITHUB CODESPACES"),
            react__WEBPACK_IMPORTED_MODULE_1___default().createElement("ul", { className: "jp-CodespaceInfo-content" },
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.repoIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, this.data.repo_name)),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.codespaceNameIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, this.data.codespace_name)),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.sourceControlIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null,
                        this.data.git_ref,
                        " \u2022 ",
                        this.data.git_behind,
                        "\u2193 ",
                        this.data.git_ahead,
                        "\u2191")),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.machineIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, this.data.machine)),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.timeoutIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null,
                        "Idle timeout ",
                        this.data.idle_timeout_minutes,
                        " minutes")),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.createdIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null, this.data.created_ago)),
                react__WEBPACK_IMPORTED_MODULE_1___default().createElement("li", null,
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_icons__WEBPACK_IMPORTED_MODULE_2__.retentionIcon.react, { className: "jp-InfoIcon" }),
                    react__WEBPACK_IMPORTED_MODULE_1___default().createElement("span", null,
                        "Retention period ",
                        this.data.retention_period_days,
                        " days")))));
    }
}



/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'codespaces-jupyterlab', // API Namespace
    endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/icons.js":
/*!**********************!*\
  !*** ./lib/icons.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "codespaceNameIcon": () => (/* binding */ codespaceNameIcon),
/* harmony export */   "createdIcon": () => (/* binding */ createdIcon),
/* harmony export */   "machineIcon": () => (/* binding */ machineIcon),
/* harmony export */   "repoIcon": () => (/* binding */ repoIcon),
/* harmony export */   "retentionIcon": () => (/* binding */ retentionIcon),
/* harmony export */   "sourceControlIcon": () => (/* binding */ sourceControlIcon),
/* harmony export */   "timeoutIcon": () => (/* binding */ timeoutIcon)
/* harmony export */ });
/* harmony import */ var _icons_vm_svg__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ../icons/vm.svg */ "./icons/vm.svg");
/* harmony import */ var _icons_book_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../icons/book.svg */ "./icons/book.svg");
/* harmony import */ var _icons_watch_svg__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../icons/watch.svg */ "./icons/watch.svg");
/* harmony import */ var _icons_repo_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../icons/repo.svg */ "./icons/repo.svg");
/* harmony import */ var _icons_tag_svg__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../icons/tag.svg */ "./icons/tag.svg");
/* harmony import */ var _icons_history_svg__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../icons/history.svg */ "./icons/history.svg");
/* harmony import */ var _icons_source_control_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../icons/source-control.svg */ "./icons/source-control.svg");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);








const createdIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'created',
    svgstr: _icons_book_svg__WEBPACK_IMPORTED_MODULE_1__["default"]
});
const timeoutIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'timeout',
    svgstr: _icons_watch_svg__WEBPACK_IMPORTED_MODULE_2__["default"]
});
const repoIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'repo',
    svgstr: _icons_repo_svg__WEBPACK_IMPORTED_MODULE_3__["default"]
});
const sourceControlIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'source-control',
    svgstr: _icons_source_control_svg__WEBPACK_IMPORTED_MODULE_4__["default"]
});
const codespaceNameIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'codespaceName',
    svgstr: _icons_tag_svg__WEBPACK_IMPORTED_MODULE_5__["default"]
});
const machineIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'machine-details',
    svgstr: _icons_vm_svg__WEBPACK_IMPORTED_MODULE_6__["default"]
});
const retentionIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'retention-period',
    svgstr: _icons_history_svg__WEBPACK_IMPORTED_MODULE_7__["default"]
});


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _CodespaceMenu__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./CodespaceMenu */ "./lib/CodespaceMenu.js");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");




/**
 * Initialization data for the codespaces-jupyterlab extension.
 */
const plugin = {
    id: 'codespaces-jupyterlab:plugin',
    autoStart: true,
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell],
    activate: (app, shell) => {
        console.log('JupyterLab extension codespaces-jupyterlab is activated!');
        (0,_handler__WEBPACK_IMPORTED_MODULE_2__.requestAPI)('hello')
            .then(data => {
            console.log(data);
            const widget = new _CodespaceMenu__WEBPACK_IMPORTED_MODULE_3__.CodespaceMenu(data);
            shell.add(widget, 'left', { rank: 700 });
        })
            .catch(reason => {
            console.error(`The codespaces_jupyterlab server extension appears to be missing.\n${reason}`);
        });
        // Reference: https://blog.ouseful.info/2022/04/28/jupyterlab-cell-status-indicator/
        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.NotebookActions.executed.connect((_, args) => {
            // The following construction seems to say 
            // something akin to: const cell = args["cell"]
            const { cell } = args;
            const { success } = args;
            var fileString = cell.parent ? "in " + cell.parent.title.label : "";
            // If we have a code cell, update the status
            if (success)
                console.log(`${cell.model.type} executed in ${fileString}`);
            else
                console.log(`cell execution error in ${fileString}`);
        });
        var mainWidgets = app.shell.widgets('main');
        console.log(mainWidgets);
        var widget = mainWidgets.next();
        while (widget) {
            console.log(widget);
            widget = mainWidgets.next();
        }
    }
};
// function __tryToGetNotebook(app: JupyterFrontEnd){
//   var notebookPanel = __getFirstVisibleNotebookPanel(app);
//   return notebookPanel
//       ?notebookPanel.content
//       :null;
// }
// function __getActivity(app: JupyterFrontEnd){
// var mainWidgets = app.shell.widgets('main');
// var widget = mainWidgets.next();
// while(widget){
//     console.log(widget);
//     widget = mainWidgets.next();
// }
// return null;
// }
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./icons/book.svg":
/*!************************!*\
  !*** ./icons/book.svg ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"22\" height=\"22\" viewBox=\"0 0 22 22\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M14.5 2H9l-.35.15-.65.64-.65-.64L7 2H1.5l-.5.5v10l.5.5h5.29l.86.85h.7l.86-.85h5.29l.5-.5v-10l-.5-.5zm-7 10.32l-.18-.17L7 12H2V3h4.79l.74.74-.03 8.58zM14 12H9l-.35.15-.14.13V3.7l.7-.7H14v9zM6 5H3v1h3V5zm0 4H3v1h3V9zM3 7h3v1H3V7zm10-2h-3v1h3V5zm-3 2h3v1h-3V7zm0 2h3v1h-3V9z\"/></svg>");

/***/ }),

/***/ "./icons/history.svg":
/*!***************************!*\
  !*** ./icons/history.svg ***!
  \***************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"22\" height=\"22\" viewBox=\"0 0 22 22\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M13.507 12.324a7 7 0 0 0 .065-8.56A7 7 0 0 0 2 4.393V2H1v3.5l.5.5H5V5H2.811a6.008 6.008 0 1 1-.135 5.77l-.887.462a7 7 0 0 0 11.718 1.092zm-3.361-.97l.708-.707L8 7.792V4H7v4l.146.354 3 3z\"/></svg>");

/***/ }),

/***/ "./icons/repo.svg":
/*!************************!*\
  !*** ./icons/repo.svg ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"22\" height=\"22\" viewBox=\"0 0 22 22\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M14 10V1.5l-.5-.5H3.74a1.9 1.9 0 0 0-.67.13 1.77 1.77 0 0 0-.94 1 1.7 1.7 0 0 0-.13.62v9.5a1.7 1.7 0 0 0 .13.67c.177.427.515.768.94.95a1.9 1.9 0 0 0 .67.13H4v-1h-.26a.72.72 0 0 1-.29-.06.74.74 0 0 1-.4-.4.93.93 0 0 1-.05-.29v-.5a.93.93 0 0 1 .05-.29.74.74 0 0 1 .4-.4.72.72 0 0 1 .286-.06H13v2H9v1h4.5l.5-.5V10zM4 10V2h9v8H4zm1-7h1v1H5V3zm0 2h1v1H5V5zm1 2H5v1h1V7zm.5 6.49L5.28 15H5v-3h3v3h-.28L6.5 13.49z\"/></svg>");

/***/ }),

/***/ "./icons/source-control.svg":
/*!**********************************!*\
  !*** ./icons/source-control.svg ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"15\" height=\"15\" viewBox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" d=\"M21.007 8.222A3.738 3.738 0 0 0 15.045 5.2a3.737 3.737 0 0 0 1.156 6.583 2.988 2.988 0 0 1-2.668 1.67h-2.99a4.456 4.456 0 0 0-2.989 1.165V7.4a3.737 3.737 0 1 0-1.494 0v9.117a3.776 3.776 0 1 0 1.816.099 2.99 2.99 0 0 1 2.668-1.667h2.99a4.484 4.484 0 0 0 4.223-3.039 3.736 3.736 0 0 0 3.25-3.687zM4.565 3.738a2.242 2.242 0 1 1 4.484 0 2.242 2.242 0 0 1-4.484 0zm4.484 16.441a2.242 2.242 0 1 1-4.484 0 2.242 2.242 0 0 1 4.484 0zm8.221-9.715a2.242 2.242 0 1 1 0-4.485 2.242 2.242 0 0 1 0 4.485z\"/></svg>");

/***/ }),

/***/ "./icons/tag.svg":
/*!***********************!*\
  !*** ./icons/tag.svg ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"22\" height=\"22\" viewBox=\"0 0 22 22\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M13.2 2H8.017l-.353.146L1 8.81v.707L6.183 14.7h.707l2.215-2.215A4.48 4.48 0 0 0 15.65 9c.027-.166.044-.332.051-.5a4.505 4.505 0 0 0-2-3.74V2.5l-.5-.5zm-.5 2.259A4.504 4.504 0 0 0 11.2 4a.5.5 0 1 0 0 1 3.5 3.5 0 0 1 1.5.338v2.138L8.775 11.4a.506.506 0 0 0-.217.217l-2.022 2.022-4.475-4.476L8.224 3H12.7v1.259zm1 1.792a3.5 3.5 0 0 1 1 2.449 3.438 3.438 0 0 1-.051.5 3.487 3.487 0 0 1-4.793 2.735l3.698-3.698.146-.354V6.051z\"/></svg>");

/***/ }),

/***/ "./icons/vm.svg":
/*!**********************!*\
  !*** ./icons/vm.svg ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"22\" height=\"22\" viewBox=\"0 0 22 22\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M14.5 2h-13l-.5.5v10l.5.5H7v1H4v1h8v-1H9v-1h5.5l.5-.5v-10l-.5-.5zM14 12H2V3h12v9z\"/></svg>");

/***/ }),

/***/ "./icons/watch.svg":
/*!*************************!*\
  !*** ./icons/watch.svg ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg width=\"22\" height=\"22\" viewBox=\"0 0 22 22\" xmlns=\"http://www.w3.org/2000/svg\" fill=\"currentColor\"><path class=\"jp-icon3\" d=\"M7.5 9h2V8H8V5.5H7v3l.5.5z\"/><path fill-rule=\"evenodd\" clip-rule=\"evenodd\" d=\"M5.5 3.669A4.998 4.998 0 0 0 3 8a4.998 4.998 0 0 0 2.5 4.331V14.5l.5.5h4l.5-.5v-2.169A4.998 4.998 0 0 0 13 8a4.998 4.998 0 0 0-2.5-4.331V1.5L10 1H6l-.5.5v2.169zM12 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0z\"/></svg>");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.d9fa1f15745fa589d9eb.js.map