"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_collaboration_lib_index_js"],{

/***/ "../../packages/collaboration/lib/awarenessmock.js":
/*!*********************************************************!*\
  !*** ../../packages/collaboration/lib/awarenessmock.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AwarenessMock": () => (/* binding */ AwarenessMock)
/* harmony export */ });
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * Default user implementation.
 */
class AwarenessMock {
    constructor(doc) {
        this.states = new Map();
        this.meta = new Map();
        this.doc = doc;
        this.clientID = doc.clientID;
    }
    setLocalState(state) {
        return;
    }
    setLocalStateField(field, value) {
        return;
    }
    getLocalState() {
        return null;
    }
    getStates() {
        return this.states;
    }
    on(name, f) {
        return;
    }
    off(name, f) {
        return;
    }
    once(name, f) {
        return;
    }
    emit(name, args) {
        return;
    }
    destroy() {
        return;
    }
}


/***/ }),

/***/ "../../packages/collaboration/lib/collaboratorspanel.js":
/*!**************************************************************!*\
  !*** ../../packages/collaboration/lib/collaboratorspanel.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CollaboratorsBody": () => (/* binding */ CollaboratorsBody),
/* harmony export */   "CollaboratorsPanel": () => (/* binding */ CollaboratorsPanel)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * The CSS class added to collaborators list container.
 */
const COLLABORATORS_LIST_CLASS = 'jp-CollaboratorsList';
/**
 * The CSS class added to each collaborator element.
 */
const COLLABORATOR_CLASS = 'jp-Collaborator';
/**
 * The CSS class added to each collaborator element.
 */
const CLICKABLE_COLLABORATOR_CLASS = 'jp-ClickableCollaborator';
/**
 * The CSS class added to each collaborator icon.
 */
const COLLABORATOR_ICON_CLASS = 'jp-CollaboratorIcon';
class CollaboratorsPanel extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Panel {
    constructor(currentUser, awareness, fileopener) {
        super({});
        /**
         * Handle collaborator change.
         */
        this._onAwarenessChanged = () => {
            const state = this._awareness.getStates();
            const collaborators = [];
            state.forEach((value, key) => {
                if (value.user.name !== this._currentUser.name) {
                    collaborators.push(value);
                }
            });
            this._body.collaborators = collaborators;
        };
        this._awareness = awareness;
        this._currentUser = currentUser;
        this._body = new CollaboratorsBody(fileopener);
        this.addWidget(this._body);
        this.update();
        this._awareness.on('change', this._onAwarenessChanged);
    }
}
/**
 * The collaborators list.
 */
class CollaboratorsBody extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ReactWidget {
    constructor(fileopener) {
        super();
        this._collaborators = [];
        this._fileopener = fileopener;
        this.addClass(COLLABORATORS_LIST_CLASS);
    }
    get collaborators() {
        return this._collaborators;
    }
    set collaborators(value) {
        this._collaborators = value;
        this.update();
    }
    render() {
        return this._collaborators.map((value, i) => {
            let canOpenCurrent = false;
            let current = '';
            let separator = '';
            let currentFileLocation = '';
            if (value.current) {
                canOpenCurrent = true;
                currentFileLocation = value.current.split(':')[1];
                current = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PathExt.basename(currentFileLocation);
                current =
                    current.length > 25 ? current.slice(0, 12).concat(`…`) : current;
                separator = '•';
            }
            const onClick = () => {
                if (canOpenCurrent) {
                    this._fileopener(currentFileLocation);
                }
            };
            const displayName = `${value.user.displayName != '' ? value.user.displayName : value.user.name} ${separator} ${current}`;
            return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: canOpenCurrent
                    ? `${CLICKABLE_COLLABORATOR_CLASS} ${COLLABORATOR_CLASS}`
                    : COLLABORATOR_CLASS, key: i, onClick: onClick },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: COLLABORATOR_ICON_CLASS, style: { backgroundColor: value.user.color } },
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement("span", null, value.user.initials)),
                react__WEBPACK_IMPORTED_MODULE_0__.createElement("span", null, displayName)));
        });
    }
}


/***/ }),

/***/ "../../packages/collaboration/lib/components.js":
/*!******************************************************!*\
  !*** ../../packages/collaboration/lib/components.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "UserIconComponent": () => (/* binding */ UserIconComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * React component for the user icon.
 *
 * @returns The React component
 */
const UserIconComponent = props => {
    const { user } = props;
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { className: "jp-UserInfo-Container" },
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("div", { title: user.displayName, className: "jp-UserInfo-Icon", style: { backgroundColor: user.color } },
            react__WEBPACK_IMPORTED_MODULE_0__.createElement("span", null, user.initials)),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("h3", null, user.displayName)));
};


/***/ }),

/***/ "../../packages/collaboration/lib/index.js":
/*!*************************************************!*\
  !*** ../../packages/collaboration/lib/index.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AwarenessMock": () => (/* reexport safe */ _awarenessmock__WEBPACK_IMPORTED_MODULE_2__.AwarenessMock),
/* harmony export */   "CollaboratorsBody": () => (/* reexport safe */ _collaboratorspanel__WEBPACK_IMPORTED_MODULE_5__.CollaboratorsBody),
/* harmony export */   "CollaboratorsPanel": () => (/* reexport safe */ _collaboratorspanel__WEBPACK_IMPORTED_MODULE_5__.CollaboratorsPanel),
/* harmony export */   "ICurrentUser": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_0__.ICurrentUser),
/* harmony export */   "IGlobalAwareness": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_0__.IGlobalAwareness),
/* harmony export */   "IUserMenu": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_0__.IUserMenu),
/* harmony export */   "RendererUserMenu": () => (/* reexport safe */ _menu__WEBPACK_IMPORTED_MODULE_3__.RendererUserMenu),
/* harmony export */   "USER": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_0__.USER),
/* harmony export */   "User": () => (/* reexport safe */ _model__WEBPACK_IMPORTED_MODULE_1__.User),
/* harmony export */   "UserInfoBody": () => (/* reexport safe */ _userinfopanel__WEBPACK_IMPORTED_MODULE_4__.UserInfoBody),
/* harmony export */   "UserInfoPanel": () => (/* reexport safe */ _userinfopanel__WEBPACK_IMPORTED_MODULE_4__.UserInfoPanel),
/* harmony export */   "UserMenu": () => (/* reexport safe */ _menu__WEBPACK_IMPORTED_MODULE_3__.UserMenu),
/* harmony export */   "getAnonymousUserName": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_6__.getAnonymousUserName),
/* harmony export */   "moonsOfJupyter": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_6__.moonsOfJupyter),
/* harmony export */   "requestAPI": () => (/* reexport safe */ _utils__WEBPACK_IMPORTED_MODULE_6__.requestAPI)
/* harmony export */ });
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./tokens */ "../../packages/collaboration/lib/tokens.js");
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./model */ "../../packages/collaboration/lib/model.js");
/* harmony import */ var _awarenessmock__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./awarenessmock */ "../../packages/collaboration/lib/awarenessmock.js");
/* harmony import */ var _menu__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./menu */ "../../packages/collaboration/lib/menu.js");
/* harmony import */ var _userinfopanel__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./userinfopanel */ "../../packages/collaboration/lib/userinfopanel.js");
/* harmony import */ var _collaboratorspanel__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./collaboratorspanel */ "../../packages/collaboration/lib/collaboratorspanel.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./utils */ "../../packages/collaboration/lib/utils.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module user
 */









/***/ }),

/***/ "../../packages/collaboration/lib/menu.js":
/*!************************************************!*\
  !*** ../../packages/collaboration/lib/menu.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RendererUserMenu": () => (/* binding */ RendererUserMenu),
/* harmony export */   "UserMenu": () => (/* binding */ UserMenu)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/virtualdom */ "webpack/sharing/consume/default/@lumino/virtualdom/@lumino/virtualdom");
/* harmony import */ var _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.






// import {requestAPI} from "./handler";
/**
 * Custom renderer for the user menu.
 */
class RendererUserMenu extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.MenuBar.Renderer {
    /**
     * Constructor of the class RendererUserMenu.
     *
     * @argument user Current user object.
     */
    constructor(user) {
        super();
        this._user = user;
    }
    /**
     * Render the virtual element for a menu bar item.
     *
     * @param data - The data to use for rendering the item.
     *
     * @returns A virtual element representing the item.
     */
    renderItem(data) {
        let className = this.createItemClass(data);
        let dataset = this.createItemDataset(data);
        let aria = this.createItemARIA(data);
        return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.li(Object.assign({ className, dataset, tabindex: '0', onfocus: data.onfocus }, aria), this._createUserIcon(), this.createShareLabel(), this.createPreviewLabel()
        // this.renderLabel(data),
        // this.renderIcon(data)
        );
    }
    /**
     * Render the label element for a menu item.
     *
     * @param data - The data to use for rendering the label.
     *
     * @returns A virtual element representing the item label.
     */
    renderLabel(data) {
        let content = this.formatLabel(data);
        return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.div({
            className: 'lm-MenuBar-itemLabel' +
                /* <DEPRECATED> */
                ' p-MenuBar-itemLabel' +
                /* </DEPRECATED> */
                ' jp-MenuBar-label'
        }, content);
    }
    /**
     * Render the user icon element for a menu item.
     *
     * @returns A virtual element representing the item label.
     */
    _createUserIcon() {
        if (this._user.isReady && this._user.avatar_url) {
            return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.div({
                className: 'lm-MenuBar-itemIcon p-MenuBar-itemIcon jp-MenuBar-imageIcon'
            }, _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.img({ src: this._user.avatar_url }));
        }
        else if (this._user.isReady) {
            return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.div({
                className: 'lm-MenuBar-itemIcon p-MenuBar-itemIcon jp-MenuBar-anonymousIcon',
                style: { backgroundColor: this._user.color }
            }, _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.span({}, this._user.initials));
        }
        else {
            return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.div({
                className: 'lm-MenuBar-itemIcon p-MenuBar-itemIcon jp-MenuBar-anonymousIcon'
            }, _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.userIcon);
        }
    }
    /**
     * Render the share icon element for a menu item.
     *
     * @returns A virtual element representing the item label.
     */
    createShareLabel() {
        const trans = _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_4__.nullTranslator.load('jupyterlab');
        return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.div({
            className: 'lm-MenuBar-itemIcon p-MenuBar-itemIcon jp-MenuBar-CommonLabel',
            onclick: async (event) => {
                let results;
                const isRunningUnderJupyterhub = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getOption('hubUser') !== '';
                if (isRunningUnderJupyterhub) {
                    // We are running on a JupyterHub, so let's just use the token set in PageConfig.
                    // Any extra servers running on the server will still need to use this token anyway,
                    // as all traffic (including any to jupyter-server-proxy) needs this token.
                    results = [{ token: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getToken() }];
                }
                else {
                    // results = await requestAPI<any>('servers');
                    results = [{ token: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getToken() }];
                }
                const links = results.map(server => {
                    // On JupyterLab, let PageConfig.getUrl do its magic.
                    // Handles workspaces, single document mode, etc
                    return _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.URLExt.normalize(`${_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getUrl({
                        workspace: _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.defaultWorkspace
                    })}?token=${server.token}`);
                });
                const entries = document.createElement('div');
                links.map(link => {
                    const p = document.createElement('p');
                    const text = document.createElement('input');
                    text.readOnly = true;
                    text.value = link;
                    text.addEventListener('click', e => {
                        e.target.select();
                    });
                    text.style.width = '100%';
                    p.appendChild(text);
                    entries.appendChild(p);
                });
                // Warn users of the security implications of using this link
                // FIXME: There *must* be a better way to create HTML
                const warning = document.createElement('div');
                const warningHeader = document.createElement('h3');
                warningHeader.innerText = trans.__('Security warning!');
                warningHeader.className = 'warningHeader';
                warning.appendChild(warningHeader);
                const messages = [
                    'Anyone with this link has full access to your notebook server, including all your files!',
                    'Please be careful who you share it with.'
                ];
                if (isRunningUnderJupyterhub) {
                    messages.push(
                    // You can restart the server to revoke the token in a JupyterHub
                    'To revoke access, go to File -> Hub Control Panel, and restart your server.');
                }
                else {
                    messages.push(
                    // Elsewhere, you *must* shut down your server - no way to revoke it
                    'Currently, there is no way to revoke access other than shutting down your server.');
                }
                messages.map(m => {
                    warning.appendChild(document.createTextNode(trans.__(m)));
                    warning.appendChild(document.createElement('br'));
                });
                entries.appendChild(warning);
                const result = await (0,_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__.showDialog)({
                    title: trans.__('Share Notebook Link'),
                    body: new _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Widget({ node: entries }),
                    buttons: [
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__.Dialog.cancelButton({ label: trans.__('Cancel') }),
                        _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__.Dialog.okButton({
                            label: trans.__('Copy Link'),
                            caption: trans.__('Copy the link to the Elixir Server')
                        })
                    ]
                });
                if (result.button.accept) {
                    _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_5__.Clipboard.copyToSystem(links[0]);
                }
            }
        }, 'Share');
    }
    /**
     * Render the preview icon element for a menu item.
     *
     * @returns A virtual element representing the item label.
     */
    createPreviewLabel() {
        return _lumino_virtualdom__WEBPACK_IMPORTED_MODULE_2__.h.div({
            className: 'lm-MenuBar-itemIcon p-MenuBar-itemIcon jp-MenuBar-CommonLabel',
            onclick: async (event) => {
                const input = document.getElementById('jp-title-panel-title-ext');
                if (input != null) {
                    const path = input.value;
                    const url = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_3__.PageConfig.getNBConvertURL({
                        path: path,
                        format: 'html',
                        download: false
                    });
                    const element = document.createElement('a');
                    element.href = url;
                    // element.download = '';
                    element.target = '_blank';
                    document.body.appendChild(element);
                    element.click();
                    document.body.removeChild(element);
                    return void 0;
                }
            }
        }, 'Preview');
    }
}
/**
 * Custom lumino Menu for the user menu.
 */
class UserMenu extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_1__.Menu {
    constructor(options) {
        super(options);
        this._updateLabel = (user) => {
            const name = user.displayName !== '' ? user.displayName : user.name;
            this.title.label = name;
            this.update();
        };
        this._user = options.user;
        const name = this._user.displayName !== '' ? this._user.displayName : this._user.name;
        this.title.label = this._user.isReady ? name : '';
        this.title.icon = _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.caretDownIcon;
        this.title.iconClass = 'jp-UserMenu-caretDownIcon';
        this._user.ready.connect(this._updateLabel);
        this._user.changed.connect(this._updateLabel);
    }
    dispose() {
        this._user.ready.disconnect(this._updateLabel);
        this._user.changed.disconnect(this._updateLabel);
    }
}


/***/ }),

/***/ "../../packages/collaboration/lib/model.js":
/*!*************************************************!*\
  !*** ../../packages/collaboration/lib/model.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "User": () => (/* binding */ User)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./tokens */ "../../packages/collaboration/lib/tokens.js");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./utils */ "../../packages/collaboration/lib/utils.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




/**
 * Default user implementation.
 */
class User {
    /**
     * Constructor of the User class.
     */
    constructor() {
        this._isReady = false;
        this._ready = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
        this._fetchUser();
        this._isReady = true;
        this._ready.emit(true);
    }
    /**
     * User's unique identifier.
     */
    get username() {
        return this._username;
    }
    /**
     * User's full name.
     */
    get name() {
        return this._name;
    }
    /**
     * Shorter version of the name for displaying it on the UI.
     */
    get displayName() {
        return this._displayName;
    }
    /**
     * User's name initials.
     */
    get initials() {
        return this._initials;
    }
    /**
     * User's cursor color and icon color if avatar_url is undefined
     * (there is no image).
     */
    get color() {
        return this._color;
    }
    set color(value) {
        this._color = value;
    }
    /**
     * Whether the user is anonymous or not.
     *
     * NOTE: Jupyter server doesn't handle user's identity so, by default every user
     * is anonymous unless a third-party extension provides the ICurrentUser token retrieving
     * the user identity from a third-party identity provider as GitHub, Google, etc.
     */
    get anonymous() {
        return this._anonymous;
    }
    /**
     * User's cursor position on the document.
     *
     * If undefined, the user is not on a document.
     */
    get cursor() {
        return this._cursor;
    }
    /**
     * Whether the user information is loaded or not.
     */
    get isReady() {
        return this._isReady;
    }
    /**
     * Signal emitted when the user's information is ready.
     */
    get ready() {
        return this._ready;
    }
    /**
     * Signal emitted when the user's information changes.
     */
    get changed() {
        return this._changed;
    }
    /**
     * Convenience method to modify the user as a JSON object.
     */
    fromJSON(user) {
        this._username = user.username;
        this._name = user.name;
        this._displayName = user.displayName;
        this._initials = user.initials;
        this._color = user.color;
        this._anonymous = user.anonymous;
        this._cursor = user.cursor;
        this._save();
    }
    /**
     * Convenience method to export the user as a JSON object.
     */
    toJSON() {
        return {
            username: this._username,
            name: this.name,
            displayName: this._displayName,
            initials: this._initials,
            color: this._color,
            anonymous: this._anonymous,
            cursor: this._cursor
        };
    }
    /**
     * Saves the user information to StateDB.
     */
    _save() {
        const { localStorage } = window;
        localStorage.setItem(_tokens__WEBPACK_IMPORTED_MODULE_2__.USER, JSON.stringify(this.toJSON()));
        this._changed.emit();
    }
    /**
     * Retrieves the user information from StateDB, or initializes
     * the user as anonymous if doesn't exists.
     */
    _fetchUser() {
        // Read username, color and initials from URL
        const urlParams = new URLSearchParams(location.search);
        let name = urlParams.get('username') || '';
        let color = urlParams.get('usercolor') || '';
        let initials = urlParams.get('initials') || '';
        const { localStorage } = window;
        const data = localStorage.getItem(_tokens__WEBPACK_IMPORTED_MODULE_2__.USER);
        if (data !== null) {
            const user = JSON.parse(data);
            this._username = user.username;
            this._name = name !== '' ? name : user.name;
            this._displayName = name !== '' ? name : user.displayName;
            this._initials = initials !== '' ? initials : user.initials;
            this._color = color !== '' ? '#' + color : user.color;
            this._anonymous = user.anonymous;
            this._cursor = user.cursor || undefined;
            if (name !== '' || color !== '') {
                this._save();
            }
        }
        else {
            // Get random values
            const anonymousName = (0,_utils__WEBPACK_IMPORTED_MODULE_3__.getAnonymousUserName)();
            this._username = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.UUID.uuid4();
            this._name = name !== '' ? name : 'Anonymous ' + anonymousName;
            this._displayName = this._name;
            this._initials =
                initials !== ''
                    ? initials
                    : `A${anonymousName.substring(0, 1).toLocaleUpperCase()}`;
            this._color = color !== '' ? '#' + color : Private.getRandomColor();
            this._anonymous = true;
            this._cursor = undefined;
            this._save();
        }
    }
}
/**
 * A namespace for module-private functionality.
 *
 * Note: We do not want to export this function
 * to move it to css variables in the Theme.
 */
var Private;
(function (Private) {
    /**
     * Predefined colors for users
     */
    const userColors = [
        'var(--jp-collaborator-color1)',
        'var(--jp-collaborator-color2)',
        'var(--jp-collaborator-color3)',
        'var(--jp-collaborator-color4)',
        'var(--jp-collaborator-color5)',
        'var(--jp-collaborator-color6)',
        'var(--jp-collaborator-color7)'
    ];
    /**
     * Get a random color from the list of colors.
     */
    Private.getRandomColor = () => userColors[Math.floor(Math.random() * userColors.length)];
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/collaboration/lib/tokens.js":
/*!**************************************************!*\
  !*** ../../packages/collaboration/lib/tokens.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ICurrentUser": () => (/* binding */ ICurrentUser),
/* harmony export */   "IGlobalAwareness": () => (/* binding */ IGlobalAwareness),
/* harmony export */   "IUserMenu": () => (/* binding */ IUserMenu),
/* harmony export */   "USER": () => (/* binding */ USER)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * An ID to track the user on StateDB.
 */
const USER = '@jupyterlab/collaboration:userDB';
/**
 * @experimental
 * @alpha
 *
 * The user token.
 *
 * NOTE: Requirer this token in your extension to access the
 * current connected user information.
 */
const ICurrentUser = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/collaboration:ICurrentUser');
/**
 * The user menu token.
 *
 * NOTE: Require this token in your extension to access the user menu
 * (top-right menu in JupyterLab's interface).
 */
const IUserMenu = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/collaboration:IUserMenu');
/**
 * The global awareness token.
 */
const IGlobalAwareness = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/collaboration:IGlobalAwareness');


/***/ }),

/***/ "../../packages/collaboration/lib/userinfopanel.js":
/*!*********************************************************!*\
  !*** ../../packages/collaboration/lib/userinfopanel.js ***!
  \*********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "UserInfoBody": () => (/* binding */ UserInfoBody),
/* harmony export */   "UserInfoPanel": () => (/* binding */ UserInfoPanel)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components */ "../../packages/collaboration/lib/components.js");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_2__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.




class UserInfoPanel extends _lumino_widgets__WEBPACK_IMPORTED_MODULE_2__.Panel {
    constructor(user) {
        super({});
        this.addClass('jp-UserInfoPanel');
        this._profile = user;
        if (this._profile.isReady) {
            this._body = new UserInfoBody(user.toJSON());
            this.addWidget(this._body);
            this.update();
        }
        else {
            this._profile.ready.connect(user => {
                this._body = new UserInfoBody(user.toJSON());
                this.addWidget(this._body);
                this.update();
            });
        }
    }
}
/**
 * A SettingsWidget for the user.
 */
class UserInfoBody extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    /**
     * Constructs a new settings widget.
     */
    constructor(user) {
        super();
        this._user = user;
    }
    get user() {
        return this._user;
    }
    set user(user) {
        this._user = user;
        this.update();
    }
    render() {
        return react__WEBPACK_IMPORTED_MODULE_1__.createElement(_components__WEBPACK_IMPORTED_MODULE_3__.UserIconComponent, { user: this._user });
    }
}


/***/ }),

/***/ "../../packages/collaboration/lib/utils.js":
/*!*************************************************!*\
  !*** ../../packages/collaboration/lib/utils.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "getAnonymousUserName": () => (/* binding */ getAnonymousUserName),
/* harmony export */   "moonsOfJupyter": () => (/* binding */ moonsOfJupyter),
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, endPoint);
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
// From https://en.wikipedia.org/wiki/Moons_of_Jupiter
const moonsOfJupyter = [
    'Metis',
    'Adrastea',
    'Amalthea',
    'Thebe',
    'Io',
    'Europa',
    'Ganymede',
    'Callisto',
    'Themisto',
    'Leda',
    'Ersa',
    'Pandia',
    'Himalia',
    'Lysithea',
    'Elara',
    'Dia',
    'Carpo',
    'Valetudo',
    'Euporie',
    'Eupheme',
    // 'S/2003 J 18',
    // 'S/2010 J 2',
    'Helike',
    // 'S/2003 J 16',
    // 'S/2003 J 2',
    'Euanthe',
    // 'S/2017 J 7',
    'Hermippe',
    'Praxidike',
    'Thyone',
    'Thelxinoe',
    // 'S/2017 J 3',
    'Ananke',
    'Mneme',
    // 'S/2016 J 1',
    'Orthosie',
    'Harpalyke',
    'Iocaste',
    // 'S/2017 J 9',
    // 'S/2003 J 12',
    // 'S/2003 J 4',
    'Erinome',
    'Aitne',
    'Herse',
    'Taygete',
    // 'S/2017 J 2',
    // 'S/2017 J 6',
    'Eukelade',
    'Carme',
    // 'S/2003 J 19',
    'Isonoe',
    // 'S/2003 J 10',
    'Autonoe',
    'Philophrosyne',
    'Cyllene',
    'Pasithee',
    // 'S/2010 J 1',
    'Pasiphae',
    'Sponde',
    // 'S/2017 J 8',
    'Eurydome',
    // 'S/2017 J 5',
    'Kalyke',
    'Hegemone',
    'Kale',
    'Kallichore',
    // 'S/2011 J 1',
    // 'S/2017 J 1',
    'Chaldene',
    'Arche',
    'Eirene',
    'Kore',
    // 'S/2011 J 2',
    // 'S/2003 J 9',
    'Megaclite',
    'Aoede',
    // 'S/2003 J 23',
    'Callirrhoe',
    'Sinope'
];
/**
 * Get a random user-name based on the moons of Jupyter.
 * This function returns names like "Anonymous Io" or "Anonymous Metis".
 */
const getAnonymousUserName = () => moonsOfJupyter[Math.floor(Math.random() * moonsOfJupyter.length)];


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfY29sbGFib3JhdGlvbl9saWJfaW5kZXhfanMuODZkNTU5ZTYxZGZmODYxMjczNDQuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7OztBQUFBLDBDQUEwQztBQUMxQywyREFBMkQ7QUFLM0Q7O0dBRUc7QUFDSSxNQUFNLGFBQWE7SUFDeEIsWUFBWSxHQUFVO1FBdUN0QixXQUFNLEdBQWtCLElBQUksR0FBRyxFQUFFLENBQUM7UUFDbEMsU0FBSSxHQUFrQixJQUFJLEdBQUcsRUFBRSxDQUFDO1FBdkM5QixJQUFJLENBQUMsR0FBRyxHQUFHLEdBQUcsQ0FBQztRQUNmLElBQUksQ0FBQyxRQUFRLEdBQUcsR0FBRyxDQUFDLFFBQVEsQ0FBQztJQUMvQixDQUFDO0lBRUQsYUFBYSxDQUFDLEtBQVU7UUFDdEIsT0FBTztJQUNULENBQUM7SUFFRCxrQkFBa0IsQ0FBQyxLQUFhLEVBQUUsS0FBVTtRQUMxQyxPQUFPO0lBQ1QsQ0FBQztJQUVELGFBQWE7UUFDWCxPQUFPLElBQUksQ0FBQztJQUNkLENBQUM7SUFFRCxTQUFTO1FBQ1AsT0FBTyxJQUFJLENBQUMsTUFBTSxDQUFDO0lBQ3JCLENBQUM7SUFFRCxFQUFFLENBQUMsSUFBWSxFQUFFLENBQU07UUFDckIsT0FBTztJQUNULENBQUM7SUFDRCxHQUFHLENBQUMsSUFBWSxFQUFFLENBQU07UUFDdEIsT0FBTztJQUNULENBQUM7SUFDRCxJQUFJLENBQUMsSUFBWSxFQUFFLENBQU07UUFDdkIsT0FBTztJQUNULENBQUM7SUFDRCxJQUFJLENBQUMsSUFBWSxFQUFFLElBQVM7UUFDMUIsT0FBTztJQUNULENBQUM7SUFDRCxPQUFPO1FBQ0wsT0FBTztJQUNULENBQUM7Q0FRRjs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDckRELDBDQUEwQztBQUMxQywyREFBMkQ7QUFFNUI7QUFJUztBQUVXO0FBSUg7QUFFaEQ7O0dBRUc7QUFDSCxNQUFNLHdCQUF3QixHQUFHLHNCQUFzQixDQUFDO0FBRXhEOztHQUVHO0FBQ0gs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O0lBQ1IsV0FBVztJQUNYLGdCQUFnQjtJQUNoQixRQUFRO0lBQ1IsT0FBTztJQUNQLGdCQUFnQjtJQUNoQixVQUFVO0lBQ1YsV0FBVztJQUNYLFNBQVM7SUFDVCxnQkFBZ0I7SUFDaEIsaUJBQWlCO0lBQ2pCLGdCQUFnQjtJQUNoQixTQUFTO0lBQ1QsT0FBTztJQUNQLE9BQU87SUFDUCxTQUFTO0lBQ1QsZ0JBQWdCO0lBQ2hCLGdCQUFnQjtJQUNoQixVQUFVO0lBQ1YsT0FBTztJQUNQLGlCQUFpQjtJQUNqQixRQUFRO0lBQ1IsaUJBQWlCO0lBQ2pCLFNBQVM7SUFDVCxlQUFlO0lBQ2YsU0FBUztJQUNULFVBQVU7SUFDVixnQkFBZ0I7SUFDaEIsVUFBVTtJQUNWLFFBQVE7SUFDUixnQkFBZ0I7SUFDaEIsVUFBVTtJQUNWLGdCQUFnQjtJQUNoQixRQUFRO0lBQ1IsVUFBVTtJQUNWLE1BQU07SUFDTixZQUFZO0lBQ1osZ0JBQWdCO0lBQ2hCLGdCQUFnQjtJQUNoQixVQUFVO0lBQ1YsT0FBTztJQUNQLFFBQVE7SUFDUixNQUFNO0lBQ04sZ0JBQWdCO0lBQ2hCLGdCQUFnQjtJQUNoQixXQUFXO0lBQ1gsT0FBTztJQUNQLGlCQUFpQjtJQUNqQixZQUFZO0lBQ1osUUFBUTtDQUNULENBQUM7QUFFRjs7O0dBR0c7QUFDSSxNQUFNLG9CQUFvQixHQUFHLEdBQVcsRUFBRSxDQUMvQyxjQUFjLENBQUMsSUFBSSxDQUFDLEtBQUssQ0FBQyxJQUFJLENBQUMsTUFBTSxFQUFFLEdBQUcsY0FBYyxDQUFDLE1BQU0sQ0FBQyxDQUFDLENBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29sbGFib3JhdGlvbi9zcmMvYXdhcmVuZXNzbW9jay50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29sbGFib3JhdGlvbi9zcmMvY29sbGFib3JhdG9yc3BhbmVsLnRzeCIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29sbGFib3JhdGlvbi9zcmMvY29tcG9uZW50cy50c3giLCJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2NvbGxhYm9yYXRpb24vc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb2xsYWJvcmF0aW9uL3NyYy9tZW51LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb2xsYWJvcmF0aW9uL3NyYy9tb2RlbC50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29sbGFib3JhdGlvbi9zcmMvdG9rZW5zLnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9jb2xsYWJvcmF0aW9uL3NyYy91c2VyaW5mb3BhbmVsLnRzeCIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvY29sbGFib3JhdGlvbi9zcmMvdXRpbHMudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgKiBhcyBZIGZyb20gJ3lqcyc7XG5pbXBvcnQgeyBJQXdhcmVuZXNzIH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIERlZmF1bHQgdXNlciBpbXBsZW1lbnRhdGlvbi5cbiAqL1xuZXhwb3J0IGNsYXNzIEF3YXJlbmVzc01vY2sgaW1wbGVtZW50cyBJQXdhcmVuZXNzIHtcbiAgY29uc3RydWN0b3IoZG9jOiBZLkRvYykge1xuICAgIHRoaXMuZG9jID0gZG9jO1xuICAgIHRoaXMuY2xpZW50SUQgPSBkb2MuY2xpZW50SUQ7XG4gIH1cblxuICBzZXRMb2NhbFN0YXRlKHN0YXRlOiBhbnkpIHtcbiAgICByZXR1cm47XG4gIH1cblxuICBzZXRMb2NhbFN0YXRlRmllbGQoZmllbGQ6IHN0cmluZywgdmFsdWU6IGFueSkge1xuICAgIHJldHVybjtcbiAgfVxuXG4gIGdldExvY2FsU3RhdGUoKTogYW55IHtcbiAgICByZXR1cm4gbnVsbDtcbiAgfVxuXG4gIGdldFN0YXRlcygpOiBhbnkge1xuICAgIHJldHVybiB0aGlzLnN0YXRlcztcbiAgfVxuXG4gIG9uKG5hbWU6IHN0cmluZywgZjogYW55KSB7XG4gICAgcmV0dXJuO1xuICB9XG4gIG9mZihuYW1lOiBzdHJpbmcsIGY6IGFueSkge1xuICAgIHJldHVybjtcbiAgfVxuICBvbmNlKG5hbWU6IHN0cmluZywgZjogYW55KSB7XG4gICAgcmV0dXJuO1xuICB9XG4gIGVtaXQobmFtZTogc3RyaW5nLCBhcmdzOiBhbnkpIHtcbiAgICByZXR1cm47XG4gIH1cbiAgZGVzdHJveSgpIHtcbiAgICByZXR1cm47XG4gIH1cblxuICBkb2M6IFkuRG9jO1xuICBjbGllbnRJRDogbnVtYmVyO1xuICBzdGF0ZXM6IE1hcDxhbnksIGFueT4gPSBuZXcgTWFwKCk7XG4gIG1ldGE6IE1hcDxhbnksIGFueT4gPSBuZXcgTWFwKCk7XG4gIF9jaGVja0ludGVydmFsOiBhbnk7XG4gIF9vYnNlcnZlcnM6IGFueTtcbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0ICogYXMgUmVhY3QgZnJvbSAncmVhY3QnO1xuXG5pbXBvcnQgeyBBd2FyZW5lc3MgfSBmcm9tICd5LXByb3RvY29scy9hd2FyZW5lc3MnO1xuXG5pbXBvcnQgeyBQYW5lbCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5cbmltcG9ydCB7IFJlYWN0V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuXG5pbXBvcnQgeyBJQ3VycmVudFVzZXIgfSBmcm9tICcuL3Rva2Vucyc7XG5pbXBvcnQgeyBJQ29sbGFib3JhdG9yQXdhcmVuZXNzIH0gZnJvbSAnLi91dGlscyc7XG5pbXBvcnQgeyBQYXRoRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIGFkZGVkIHRvIGNvbGxhYm9yYXRvcnMgbGlzdCBjb250YWluZXIuXG4gKi9cbmNvbnN0IENPTExBQk9SQVRPUlNfTElTVF9DTEFTUyA9ICdqcC1Db2xsYWJvcmF0b3JzTGlzdCc7XG5cbi8qKlxuICogVGhlIENTUyBjbGFzcyBhZGRlZCB0byBlYWNoIGNvbGxhYm9yYXRvciBlbGVtZW50LlxuICovXG5jb25zdCBDT0xMQUJPUkFUT1JfQ0xBU1MgPSAnanAtQ29sbGFib3JhdG9yJztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIGFkZGVkIHRvIGVhY2ggY29sbGFib3JhdG9yIGVsZW1lbnQuXG4gKi9cbmNvbnN0IENMSUNLQUJMRV9DT0xMQUJPUkFUT1JfQ0xBU1MgPSAnanAtQ2xpY2thYmxlQ29sbGFib3JhdG9yJztcblxuLyoqXG4gKiBUaGUgQ1NTIGNsYXNzIGFkZGVkIHRvIGVhY2ggY29sbGFib3JhdG9yIGljb24uXG4gKi9cbmNvbnN0IENPTExBQk9SQVRPUl9JQ09OX0NMQVNTID0gJ2pwLUNvbGxhYm9yYXRvckljb24nO1xuXG5leHBvcnQgY2xhc3MgQ29sbGFib3JhdG9yc1BhbmVsIGV4dGVuZHMgUGFuZWwge1xuICBwcml2YXRlIF9jdXJyZW50VXNlcjogSUN1cnJlbnRVc2VyO1xuICBwcml2YXRlIF9hd2FyZW5lc3M6IEF3YXJlbmVzcztcbiAgcHJpdmF0ZSBfYm9keTogQ29sbGFib3JhdG9yc0JvZHk7XG5cbiAgY29uc3RydWN0b3IoXG4gICAgY3VycmVudFVzZXI6IElDdXJyZW50VXNlcixcbiAgICBhd2FyZW5lc3M6IEF3YXJlbmVzcyxcbiAgICBmaWxlb3BlbmVyOiAocGF0aDogc3RyaW5nKSA9PiB2b2lkXG4gICkge1xuICAgIHN1cGVyKHt9KTtcblxuICAgIHRoaXMuX2F3YXJlbmVzcyA9IGF3YXJlbmVzcztcblxuICAgIHRoaXMuX2N1cnJlbnRVc2VyID0gY3VycmVudFVzZXI7XG5cbiAgICB0aGlzLl9ib2R5ID0gbmV3IENvbGxhYm9yYXRvcnNCb2R5KGZpbGVvcGVuZXIpO1xuICAgIHRoaXMuYWRkV2lkZ2V0KHRoaXMuX2JvZHkpO1xuICAgIHRoaXMudXBkYXRlKCk7XG5cbiAgICB0aGlzLl9hd2FyZW5lc3Mub24oJ2NoYW5nZScsIHRoaXMuX29uQXdhcmVuZXNzQ2hhbmdlZCk7XG4gIH1cblxuICAvKipcbiAgICogSGFuZGxlIGNvbGxhYm9yYXRvciBjaGFuZ2UuXG4gICAqL1xuICBwcml2YXRlIF9vbkF3YXJlbmVzc0NoYW5nZWQgPSAoKSA9PiB7XG4gICAgY29uc3Qgc3RhdGUgPSB0aGlzLl9hd2FyZW5lc3MuZ2V0U3RhdGVzKCk7XG4gICAgY29uc3QgY29sbGFib3JhdG9yczogSUNvbGxhYm9yYXRvckF3YXJlbmVzc1tdID0gW107XG5cbiAgICBzdGF0ZS5mb3JFYWNoKCh2YWx1ZTogSUNvbGxhYm9yYXRvckF3YXJlbmVzcywga2V5OiBhbnkpID0+IHtcbiAgICAgIGlmICh2YWx1ZS51c2VyLm5hbWUgIT09IHRoaXMuX2N1cnJlbnRVc2VyLm5hbWUpIHtcbiAgICAgICAgY29sbGFib3JhdG9ycy5wdXNoKHZhbHVlKTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIHRoaXMuX2JvZHkuY29sbGFib3JhdG9ycyA9IGNvbGxhYm9yYXRvcnM7XG4gIH07XG59XG5cbi8qKlxuICogVGhlIGNvbGxhYm9yYXRvcnMgbGlzdC5cbiAqL1xuZXhwb3J0IGNsYXNzIENvbGxhYm9yYXRvcnNCb2R5IGV4dGVuZHMgUmVhY3RXaWRnZXQge1xuICBwcml2YXRlIF9jb2xsYWJvcmF0b3JzOiBJQ29sbGFib3JhdG9yQXdhcmVuZXNzW10gPSBbXTtcbiAgcHJpdmF0ZSBfZmlsZW9wZW5lcjogKHBhdGg6IHN0cmluZykgPT4gdm9pZDtcblxuICBjb25zdHJ1Y3RvcihmaWxlb3BlbmVyOiAocGF0aDogc3RyaW5nKSA9PiB2b2lkKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLl9maWxlb3BlbmVyID0gZmlsZW9wZW5lcjtcbiAgICB0aGlzLmFkZENsYXNzKENPTExBQk9SQVRPUlNfTElTVF9DTEFTUyk7XG4gIH1cblxuICBnZXQgY29sbGFib3JhdG9ycygpOiBJQ29sbGFib3JhdG9yQXdhcmVuZXNzW10ge1xuICAgIHJldHVybiB0aGlzLl9jb2xsYWJvcmF0b3JzO1xuICB9XG5cbiAgc2V0IGNvbGxhYm9yYXRvcnModmFsdWU6IElDb2xsYWJvcmF0b3JBd2FyZW5lc3NbXSkge1xuICAgIHRoaXMuX2NvbGxhYm9yYXRvcnMgPSB2YWx1ZTtcbiAgICB0aGlzLnVwZGF0ZSgpO1xuICB9XG5cbiAgcmVuZGVyKCk6IFJlYWN0LlJlYWN0RWxlbWVudDxhbnk+W10ge1xuICAgIHJldHVybiB0aGlzLl9jb2xsYWJvcmF0b3JzLm1hcCgodmFsdWUsIGkpID0+IHtcbiAgICAgIGxldCBjYW5PcGVuQ3VycmVudCA9IGZhbHNlO1xuICAgICAgbGV0IGN1cnJlbnQgPSAnJztcbiAgICAgIGxldCBzZXBhcmF0b3IgPSAnJztcbiAgICAgIGxldCBjdXJyZW50RmlsZUxvY2F0aW9uID0gJyc7XG5cbiAgICAgIGlmICh2YWx1ZS5jdXJyZW50KSB7XG4gICAgICAgIGNhbk9wZW5DdXJyZW50ID0gdHJ1ZTtcbiAgICAgICAgY3VycmVudEZpbGVMb2NhdGlvbiA9IHZhbHVlLmN1cnJlbnQuc3BsaXQoJzonKVsxXTtcblxuICAgICAgICBjdXJyZW50ID0gUGF0aEV4dC5iYXNlbmFtZShjdXJyZW50RmlsZUxvY2F0aW9uKTtcbiAgICAgICAgY3VycmVudCA9XG4gICAgICAgICAgY3VycmVudC5sZW5ndGggPiAyNSA/IGN1cnJlbnQuc2xpY2UoMCwgMTIpLmNvbmNhdChg4oCmYCkgOiBjdXJyZW50O1xuICAgICAgICBzZXBhcmF0b3IgPSAn4oCiJztcbiAgICAgIH1cblxuICAgICAgY29uc3Qgb25DbGljayA9ICgpID0+IHtcbiAgICAgICAgaWYgKGNhbk9wZW5DdXJyZW50KSB7XG4gICAgICAgICAgdGhpcy5fZmlsZW9wZW5lcihjdXJyZW50RmlsZUxvY2F0aW9uKTtcbiAgICAgICAgfVxuICAgICAgfTtcblxuICAgICAgY29uc3QgZGlzcGxheU5hbWUgPSBgJHtcbiAgICAgICAgdmFsdWUudXNlci5kaXNwbGF5TmFtZSAhPSAnJyA/IHZhbHVlLnVzZXIuZGlzcGxheU5hbWUgOiB2YWx1ZS51c2VyLm5hbWVcbiAgICAgIH0gJHtzZXBhcmF0b3J9ICR7Y3VycmVudH1gO1xuXG4gICAgICByZXR1cm4gKFxuICAgICAgICA8ZGl2XG4gICAgICAgICAgY2xhc3NOYW1lPXtcbiAgICAgICAgICAgIGNhbk9wZW5DdXJyZW50XG4gICAgICAgICAgICAgID8gYCR7Q0xJQ0tBQkxFX0NPTExBQk9SQVRPUl9DTEFTU30gJHtDT0xMQUJPUkFUT1JfQ0xBU1N9YFxuICAgICAgICAgICAgICA6IENPTExBQk9SQVRPUl9DTEFTU1xuICAgICAgICAgIH1cbiAgICAgICAgICBrZXk9e2l9XG4gICAgICAgICAgb25DbGljaz17b25DbGlja31cbiAgICAgICAgPlxuICAgICAgICAgIDxkaXZcbiAgICAgICAgICAgIGNsYXNzTmFtZT17Q09MTEFCT1JBVE9SX0lDT05fQ0xBU1N9XG4gICAgICAgICAgICBzdHlsZT17eyBiYWNrZ3JvdW5kQ29sb3I6IHZhbHVlLnVzZXIuY29sb3IgfX1cbiAgICAgICAgICA+XG4gICAgICAgICAgICA8c3Bhbj57dmFsdWUudXNlci5pbml0aWFsc308L3NwYW4+XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgPHNwYW4+e2Rpc3BsYXlOYW1lfTwvc3Bhbj5cbiAgICAgICAgPC9kaXY+XG4gICAgICApO1xuICAgIH0pO1xuICB9XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCAqIGFzIFJlYWN0IGZyb20gJ3JlYWN0JztcblxuaW1wb3J0IHsgSVVzZXIgfSBmcm9tICcuL3Rva2Vucyc7XG5cbnR5cGUgUHJvcHMgPSB7XG4gIHVzZXI6IElVc2VyLlVzZXI7XG59O1xuXG4vKipcbiAqIFJlYWN0IGNvbXBvbmVudCBmb3IgdGhlIHVzZXIgaWNvbi5cbiAqXG4gKiBAcmV0dXJucyBUaGUgUmVhY3QgY29tcG9uZW50XG4gKi9cbmV4cG9ydCBjb25zdCBVc2VySWNvbkNvbXBvbmVudDogUmVhY3QuRkM8UHJvcHM+ID0gcHJvcHMgPT4ge1xuICBjb25zdCB7IHVzZXIgfSA9IHByb3BzO1xuXG4gIHJldHVybiAoXG4gICAgPGRpdiBjbGFzc05hbWU9XCJqcC1Vc2VySW5mby1Db250YWluZXJcIj5cbiAgICAgIDxkaXZcbiAgICAgICAgdGl0bGU9e3VzZXIuZGlzcGxheU5hbWV9XG4gICAgICAgIGNsYXNzTmFtZT1cImpwLVVzZXJJbmZvLUljb25cIlxuICAgICAgICBzdHlsZT17eyBiYWNrZ3JvdW5kQ29sb3I6IHVzZXIuY29sb3IgfX1cbiAgICAgID5cbiAgICAgICAgPHNwYW4+e3VzZXIuaW5pdGlhbHN9PC9zcGFuPlxuICAgICAgPC9kaXY+XG4gICAgICA8aDM+e3VzZXIuZGlzcGxheU5hbWV9PC9oMz5cbiAgICA8L2Rpdj5cbiAgKTtcbn07XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSB1c2VyXG4gKi9cblxuZXhwb3J0ICogZnJvbSAnLi90b2tlbnMnO1xuZXhwb3J0ICogZnJvbSAnLi9tb2RlbCc7XG5leHBvcnQgKiBmcm9tICcuL2F3YXJlbmVzc21vY2snO1xuZXhwb3J0ICogZnJvbSAnLi9tZW51JztcbmV4cG9ydCAqIGZyb20gJy4vdXNlcmluZm9wYW5lbCc7XG5leHBvcnQgKiBmcm9tICcuL2NvbGxhYm9yYXRvcnNwYW5lbCc7XG5leHBvcnQgKiBmcm9tICcuL3V0aWxzJztcbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgY2FyZXREb3duSWNvbiwgdXNlckljb24gfSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IE1lbnUsIE1lbnVCYXIsIFdpZGdldCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5pbXBvcnQgeyBoLCBWaXJ0dWFsRWxlbWVudCB9IGZyb20gJ0BsdW1pbm8vdmlydHVhbGRvbSc7XG5pbXBvcnQgeyBQYWdlQ29uZmlnLCBVUkxFeHQgfSBmcm9tICdAanVweXRlcmxhYi9jb3JldXRpbHMnO1xuaW1wb3J0IHsgbnVsbFRyYW5zbGF0b3IgfSBmcm9tICdAanVweXRlcmxhYi90cmFuc2xhdGlvbic7XG5pbXBvcnQgeyBDbGlwYm9hcmQsIERpYWxvZywgc2hvd0RpYWxvZyB9IGZyb20gJ0BqdXB5dGVybGFiL2FwcHV0aWxzJztcblxuaW1wb3J0IHsgSUN1cnJlbnRVc2VyIH0gZnJvbSAnLi90b2tlbnMnO1xuLy8gaW1wb3J0IHtyZXF1ZXN0QVBJfSBmcm9tIFwiLi9oYW5kbGVyXCI7XG5cbi8qKlxuICogQ3VzdG9tIHJlbmRlcmVyIGZvciB0aGUgdXNlciBtZW51LlxuICovXG5leHBvcnQgY2xhc3MgUmVuZGVyZXJVc2VyTWVudSBleHRlbmRzIE1lbnVCYXIuUmVuZGVyZXIge1xuICBwcml2YXRlIF91c2VyOiBJQ3VycmVudFVzZXI7XG5cbiAgLyoqXG4gICAqIENvbnN0cnVjdG9yIG9mIHRoZSBjbGFzcyBSZW5kZXJlclVzZXJNZW51LlxuICAgKlxuICAgKiBAYXJndW1lbnQgdXNlciBDdXJyZW50IHVzZXIgb2JqZWN0LlxuICAgKi9cbiAgY29uc3RydWN0b3IodXNlcjogSUN1cnJlbnRVc2VyKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLl91c2VyID0gdXNlcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgdGhlIHZpcnR1YWwgZWxlbWVudCBmb3IgYSBtZW51IGJhciBpdGVtLlxuICAgKlxuICAgKiBAcGFyYW0gZGF0YSAtIFRoZSBkYXRhIHRvIHVzZSBmb3IgcmVuZGVyaW5nIHRoZSBpdGVtLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHZpcnR1YWwgZWxlbWVudCByZXByZXNlbnRpbmcgdGhlIGl0ZW0uXG4gICAqL1xuICByZW5kZXJJdGVtKGRhdGE6IE1lbnVCYXIuSVJlbmRlckRhdGEpOiBWaXJ0dWFsRWxlbWVudCB7XG4gICAgbGV0IGNsYXNzTmFtZSA9IHRoaXMuY3JlYXRlSXRlbUNsYXNzKGRhdGEpO1xuICAgIGxldCBkYXRhc2V0ID0gdGhpcy5jcmVhdGVJdGVtRGF0YXNldChkYXRhKTtcbiAgICBsZXQgYXJpYSA9IHRoaXMuY3JlYXRlSXRlbUFSSUEoZGF0YSk7XG4gICAgcmV0dXJuIGgubGkoXG4gICAgICB7IGNsYXNzTmFtZSwgZGF0YXNldCwgdGFiaW5kZXg6ICcwJywgb25mb2N1czogZGF0YS5vbmZvY3VzLCAuLi5hcmlhIH0sXG4gICAgICB0aGlzLl9jcmVhdGVVc2VySWNvbigpLFxuICAgICAgdGhpcy5jcmVhdGVTaGFyZUxhYmVsKCksXG4gICAgICB0aGlzLmNyZWF0ZVByZXZpZXdMYWJlbCgpXG4gICAgICAvLyB0aGlzLnJlbmRlckxhYmVsKGRhdGEpLFxuICAgICAgLy8gdGhpcy5yZW5kZXJJY29uKGRhdGEpXG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgdGhlIGxhYmVsIGVsZW1lbnQgZm9yIGEgbWVudSBpdGVtLlxuICAgKlxuICAgKiBAcGFyYW0gZGF0YSAtIFRoZSBkYXRhIHRvIHVzZSBmb3IgcmVuZGVyaW5nIHRoZSBsYWJlbC5cbiAgICpcbiAgICogQHJldHVybnMgQSB2aXJ0dWFsIGVsZW1lbnQgcmVwcmVzZW50aW5nIHRoZSBpdGVtIGxhYmVsLlxuICAgKi9cbiAgcmVuZGVyTGFiZWwoZGF0YTogTWVudUJhci5JUmVuZGVyRGF0YSk6IFZpcnR1YWxFbGVtZW50IHtcbiAgICBsZXQgY29udGVudCA9IHRoaXMuZm9ybWF0TGFiZWwoZGF0YSk7XG4gICAgcmV0dXJuIGguZGl2KFxuICAgICAge1xuICAgICAgICBjbGFzc05hbWU6XG4gICAgICAgICAgJ2xtLU1lbnVCYXItaXRlbUxhYmVsJyArXG4gICAgICAgICAgLyogPERFUFJFQ0FURUQ+ICovXG4gICAgICAgICAgJyBwLU1lbnVCYXItaXRlbUxhYmVsJyArXG4gICAgICAgICAgLyogPC9ERVBSRUNBVEVEPiAqL1xuICAgICAgICAgICcganAtTWVudUJhci1sYWJlbCdcbiAgICAgIH0sXG4gICAgICBjb250ZW50XG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgdGhlIHVzZXIgaWNvbiBlbGVtZW50IGZvciBhIG1lbnUgaXRlbS5cbiAgICpcbiAgICogQHJldHVybnMgQSB2aXJ0dWFsIGVsZW1lbnQgcmVwcmVzZW50aW5nIHRoZSBpdGVtIGxhYmVsLlxuICAgKi9cbiAgcHJpdmF0ZSBfY3JlYXRlVXNlckljb24oKTogVmlydHVhbEVsZW1lbnQge1xuICAgIGlmICh0aGlzLl91c2VyLmlzUmVhZHkgJiYgdGhpcy5fdXNlci5hdmF0YXJfdXJsKSB7XG4gICAgICByZXR1cm4gaC5kaXYoXG4gICAgICAgIHtcbiAgICAgICAgICBjbGFzc05hbWU6XG4gICAgICAgICAgICAnbG0tTWVudUJhci1pdGVtSWNvbiBwLU1lbnVCYXItaXRlbUljb24ganAtTWVudUJhci1pbWFnZUljb24nXG4gICAgICAgIH0sXG4gICAgICAgIGguaW1nKHsgc3JjOiB0aGlzLl91c2VyLmF2YXRhcl91cmwgfSlcbiAgICAgICk7XG4gICAgfSBlbHNlIGlmICh0aGlzLl91c2VyLmlzUmVhZHkpIHtcbiAgICAgIHJldHVybiBoLmRpdihcbiAgICAgICAge1xuICAgICAgICAgIGNsYXNzTmFtZTpcbiAgICAgICAgICAgICdsbS1NZW51QmFyLWl0ZW1JY29uIHAtTWVudUJhci1pdGVtSWNvbiBqcC1NZW51QmFyLWFub255bW91c0ljb24nLFxuICAgICAgICAgIHN0eWxlOiB7IGJhY2tncm91bmRDb2xvcjogdGhpcy5fdXNlci5jb2xvciB9XG4gICAgICAgIH0sXG4gICAgICAgIGguc3Bhbih7fSwgdGhpcy5fdXNlci5pbml0aWFscylcbiAgICAgICk7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJldHVybiBoLmRpdihcbiAgICAgICAge1xuICAgICAgICAgIGNsYXNzTmFtZTpcbiAgICAgICAgICAgICdsbS1NZW51QmFyLWl0ZW1JY29uIHAtTWVudUJhci1pdGVtSWNvbiBqcC1NZW51QmFyLWFub255bW91c0ljb24nXG4gICAgICAgIH0sXG4gICAgICAgIHVzZXJJY29uXG4gICAgICApO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXIgdGhlIHNoYXJlIGljb24gZWxlbWVudCBmb3IgYSBtZW51IGl0ZW0uXG4gICAqXG4gICAqIEByZXR1cm5zIEEgdmlydHVhbCBlbGVtZW50IHJlcHJlc2VudGluZyB0aGUgaXRlbSBsYWJlbC5cbiAgICovXG4gIGNyZWF0ZVNoYXJlTGFiZWwoKTogVmlydHVhbEVsZW1lbnQge1xuICAgIGNvbnN0IHRyYW5zID0gbnVsbFRyYW5zbGF0b3IubG9hZCgnanVweXRlcmxhYicpO1xuICAgIHJldHVybiBoLmRpdihcbiAgICAgIHtcbiAgICAgICAgY2xhc3NOYW1lOlxuICAgICAgICAgICdsbS1NZW51QmFyLWl0ZW1JY29uIHAtTWVudUJhci1pdGVtSWNvbiBqcC1NZW51QmFyLUNvbW1vbkxhYmVsJyxcbiAgICAgICAgb25jbGljazogYXN5bmMgZXZlbnQgPT4ge1xuICAgICAgICAgIGxldCByZXN1bHRzOiB7IHRva2VuOiBzdHJpbmcgfVtdO1xuICAgICAgICAgIGNvbnN0IGlzUnVubmluZ1VuZGVySnVweXRlcmh1YiA9XG4gICAgICAgICAgICBQYWdlQ29uZmlnLmdldE9wdGlvbignaHViVXNlcicpICE9PSAnJztcbiAgICAgICAgICBpZiAoaXNSdW5uaW5nVW5kZXJKdXB5dGVyaHViKSB7XG4gICAgICAgICAgICAvLyBXZSBhcmUgcnVubmluZyBvbiBhIEp1cHl0ZXJIdWIsIHNvIGxldCdzIGp1c3QgdXNlIHRoZSB0b2tlbiBzZXQgaW4gUGFnZUNvbmZpZy5cbiAgICAgICAgICAgIC8vIEFueSBleHRyYSBzZXJ2ZXJzIHJ1bm5pbmcgb24gdGhlIHNlcnZlciB3aWxsIHN0aWxsIG5lZWQgdG8gdXNlIHRoaXMgdG9rZW4gYW55d2F5LFxuICAgICAgICAgICAgLy8gYXMgYWxsIHRyYWZmaWMgKGluY2x1ZGluZyBhbnkgdG8ganVweXRlci1zZXJ2ZXItcHJveHkpIG5lZWRzIHRoaXMgdG9rZW4uXG4gICAgICAgICAgICByZXN1bHRzID0gW3sgdG9rZW46IFBhZ2VDb25maWcuZ2V0VG9rZW4oKSB9XTtcbiAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgLy8gcmVzdWx0cyA9IGF3YWl0IHJlcXVlc3RBUEk8YW55Pignc2VydmVycycpO1xuICAgICAgICAgICAgcmVzdWx0cyA9IFt7IHRva2VuOiBQYWdlQ29uZmlnLmdldFRva2VuKCkgfV07XG4gICAgICAgICAgfVxuXG4gICAgICAgICAgY29uc3QgbGlua3MgPSByZXN1bHRzLm1hcChzZXJ2ZXIgPT4ge1xuICAgICAgICAgICAgLy8gT24gSnVweXRlckxhYiwgbGV0IFBhZ2VDb25maWcuZ2V0VXJsIGRvIGl0cyBtYWdpYy5cbiAgICAgICAgICAgIC8vIEhhbmRsZXMgd29ya3NwYWNlcywgc2luZ2xlIGRvY3VtZW50IG1vZGUsIGV0Y1xuICAgICAgICAgICAgcmV0dXJuIFVSTEV4dC5ub3JtYWxpemUoXG4gICAgICAgICAgICAgIGAke1BhZ2VDb25maWcuZ2V0VXJsKHtcbiAgICAgICAgICAgICAgICB3b3Jrc3BhY2U6IFBhZ2VDb25maWcuZGVmYXVsdFdvcmtzcGFjZVxuICAgICAgICAgICAgICB9KX0/dG9rZW49JHtzZXJ2ZXIudG9rZW59YFxuICAgICAgICAgICAgKTtcbiAgICAgICAgICB9KTtcblxuICAgICAgICAgIGNvbnN0IGVudHJpZXMgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcbiAgICAgICAgICBsaW5rcy5tYXAobGluayA9PiB7XG4gICAgICAgICAgICBjb25zdCBwID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgncCcpO1xuICAgICAgICAgICAgY29uc3QgdGV4dDogSFRNTElucHV0RWxlbWVudCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2lucHV0Jyk7XG4gICAgICAgICAgICB0ZXh0LnJlYWRPbmx5ID0gdHJ1ZTtcbiAgICAgICAgICAgIHRleHQudmFsdWUgPSBsaW5rO1xuICAgICAgICAgICAgdGV4dC5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIGUgPT4ge1xuICAgICAgICAgICAgICAoZS50YXJnZXQgYXMgSFRNTElucHV0RWxlbWVudCkuc2VsZWN0KCk7XG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIHRleHQuc3R5bGUud2lkdGggPSAnMTAwJSc7XG4gICAgICAgICAgICBwLmFwcGVuZENoaWxkKHRleHQpO1xuICAgICAgICAgICAgZW50cmllcy5hcHBlbmRDaGlsZChwKTtcbiAgICAgICAgICB9KTtcblxuICAgICAgICAgIC8vIFdhcm4gdXNlcnMgb2YgdGhlIHNlY3VyaXR5IGltcGxpY2F0aW9ucyBvZiB1c2luZyB0aGlzIGxpbmtcbiAgICAgICAgICAvLyBGSVhNRTogVGhlcmUgKm11c3QqIGJlIGEgYmV0dGVyIHdheSB0byBjcmVhdGUgSFRNTFxuICAgICAgICAgIGNvbnN0IHdhcm5pbmcgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdkaXYnKTtcblxuICAgICAgICAgIGNvbnN0IHdhcm5pbmdIZWFkZXIgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdoMycpO1xuICAgICAgICAgIHdhcm5pbmdIZWFkZXIuaW5uZXJUZXh0ID0gdHJhbnMuX18oJ1NlY3VyaXR5IHdhcm5pbmchJyk7XG4gICAgICAgICAgd2FybmluZ0hlYWRlci5jbGFzc05hbWUgPSAnd2FybmluZ0hlYWRlcic7XG4gICAgICAgICAgd2FybmluZy5hcHBlbmRDaGlsZCh3YXJuaW5nSGVhZGVyKTtcblxuICAgICAgICAgIGNvbnN0IG1lc3NhZ2VzID0gW1xuICAgICAgICAgICAgJ0FueW9uZSB3aXRoIHRoaXMgbGluayBoYXMgZnVsbCBhY2Nlc3MgdG8geW91ciBub3RlYm9vayBzZXJ2ZXIsIGluY2x1ZGluZyBhbGwgeW91ciBmaWxlcyEnLFxuICAgICAgICAgICAgJ1BsZWFzZSBiZSBjYXJlZnVsIHdobyB5b3Ugc2hhcmUgaXQgd2l0aC4nXG4gICAgICAgICAgXTtcbiAgICAgICAgICBpZiAoaXNSdW5uaW5nVW5kZXJKdXB5dGVyaHViKSB7XG4gICAgICAgICAgICBtZXNzYWdlcy5wdXNoKFxuICAgICAgICAgICAgICAvLyBZb3UgY2FuIHJlc3RhcnQgdGhlIHNlcnZlciB0byByZXZva2UgdGhlIHRva2VuIGluIGEgSnVweXRlckh1YlxuICAgICAgICAgICAgICAnVG8gcmV2b2tlIGFjY2VzcywgZ28gdG8gRmlsZSAtPiBIdWIgQ29udHJvbCBQYW5lbCwgYW5kIHJlc3RhcnQgeW91ciBzZXJ2ZXIuJ1xuICAgICAgICAgICAgKTtcbiAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgbWVzc2FnZXMucHVzaChcbiAgICAgICAgICAgICAgLy8gRWxzZXdoZXJlLCB5b3UgKm11c3QqIHNodXQgZG93biB5b3VyIHNlcnZlciAtIG5vIHdheSB0byByZXZva2UgaXRcbiAgICAgICAgICAgICAgJ0N1cnJlbnRseSwgdGhlcmUgaXMgbm8gd2F5IHRvIHJldm9rZSBhY2Nlc3Mgb3RoZXIgdGhhbiBzaHV0dGluZyBkb3duIHlvdXIgc2VydmVyLidcbiAgICAgICAgICAgICk7XG4gICAgICAgICAgfVxuICAgICAgICAgIG1lc3NhZ2VzLm1hcChtID0+IHtcbiAgICAgICAgICAgIHdhcm5pbmcuYXBwZW5kQ2hpbGQoZG9jdW1lbnQuY3JlYXRlVGV4dE5vZGUodHJhbnMuX18obSkpKTtcbiAgICAgICAgICAgIHdhcm5pbmcuYXBwZW5kQ2hpbGQoZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnYnInKSk7XG4gICAgICAgICAgfSk7XG5cbiAgICAgICAgICBlbnRyaWVzLmFwcGVuZENoaWxkKHdhcm5pbmcpO1xuXG4gICAgICAgICAgY29uc3QgcmVzdWx0ID0gYXdhaXQgc2hvd0RpYWxvZyh7XG4gICAgICAgICAgICB0aXRsZTogdHJhbnMuX18oJ1NoYXJlIE5vdGVib29rIExpbmsnKSxcbiAgICAgICAgICAgIGJvZHk6IG5ldyBXaWRnZXQoeyBub2RlOiBlbnRyaWVzIH0pLFxuICAgICAgICAgICAgYnV0dG9uczogW1xuICAgICAgICAgICAgICBEaWFsb2cuY2FuY2VsQnV0dG9uKHsgbGFiZWw6IHRyYW5zLl9fKCdDYW5jZWwnKSB9KSxcbiAgICAgICAgICAgICAgRGlhbG9nLm9rQnV0dG9uKHtcbiAgICAgICAgICAgICAgICBsYWJlbDogdHJhbnMuX18oJ0NvcHkgTGluaycpLFxuICAgICAgICAgICAgICAgIGNhcHRpb246IHRyYW5zLl9fKCdDb3B5IHRoZSBsaW5rIHRvIHRoZSBFbGl4aXIgU2VydmVyJylcbiAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgIF1cbiAgICAgICAgICB9KTtcblxuICAgICAgICAgIGlmIChyZXN1bHQuYnV0dG9uLmFjY2VwdCkge1xuICAgICAgICAgICAgQ2xpcGJvYXJkLmNvcHlUb1N5c3RlbShsaW5rc1swXSk7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9LFxuICAgICAgJ1NoYXJlJ1xuICAgICk7XG4gIH1cblxuICAvKipcbiAgICogUmVuZGVyIHRoZSBwcmV2aWV3IGljb24gZWxlbWVudCBmb3IgYSBtZW51IGl0ZW0uXG4gICAqXG4gICAqIEByZXR1cm5zIEEgdmlydHVhbCBlbGVtZW50IHJlcHJlc2VudGluZyB0aGUgaXRlbSBsYWJlbC5cbiAgICovXG4gIGNyZWF0ZVByZXZpZXdMYWJlbCgpOiBWaXJ0dWFsRWxlbWVudCB7XG4gICAgcmV0dXJuIGguZGl2KFxuICAgICAge1xuICAgICAgICBjbGFzc05hbWU6XG4gICAgICAgICAgJ2xtLU1lbnVCYXItaXRlbUljb24gcC1NZW51QmFyLWl0ZW1JY29uIGpwLU1lbnVCYXItQ29tbW9uTGFiZWwnLFxuICAgICAgICBvbmNsaWNrOiBhc3luYyBldmVudCA9PiB7XG4gICAgICAgICAgY29uc3QgaW5wdXQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcbiAgICAgICAgICAgICdqcC10aXRsZS1wYW5lbC10aXRsZS1leHQnXG4gICAgICAgICAgKSBhcyBIVE1MSW5wdXRFbGVtZW50IHwgbnVsbDtcbiAgICAgICAgICBpZiAoaW5wdXQgIT0gbnVsbCkge1xuICAgICAgICAgICAgY29uc3QgcGF0aCA9IGlucHV0LnZhbHVlO1xuICAgICAgICAgICAgY29uc3QgdXJsID0gUGFnZUNvbmZpZy5nZXROQkNvbnZlcnRVUkwoe1xuICAgICAgICAgICAgICBwYXRoOiBwYXRoLFxuICAgICAgICAgICAgICBmb3JtYXQ6ICdodG1sJyxcbiAgICAgICAgICAgICAgZG93bmxvYWQ6IGZhbHNlXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIGNvbnN0IGVsZW1lbnQgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdhJyk7XG4gICAgICAgICAgICBlbGVtZW50LmhyZWYgPSB1cmw7XG4gICAgICAgICAgICAvLyBlbGVtZW50LmRvd25sb2FkID0gJyc7XG4gICAgICAgICAgICBlbGVtZW50LnRhcmdldCA9ICdfYmxhbmsnO1xuICAgICAgICAgICAgZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChlbGVtZW50KTtcbiAgICAgICAgICAgIGVsZW1lbnQuY2xpY2soKTtcbiAgICAgICAgICAgIGRvY3VtZW50LmJvZHkucmVtb3ZlQ2hpbGQoZWxlbWVudCk7XG4gICAgICAgICAgICByZXR1cm4gdm9pZCAwO1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgfSxcbiAgICAgICdQcmV2aWV3J1xuICAgICk7XG4gIH1cbn1cblxuLyoqXG4gKiBDdXN0b20gbHVtaW5vIE1lbnUgZm9yIHRoZSB1c2VyIG1lbnUuXG4gKi9cbmV4cG9ydCBjbGFzcyBVc2VyTWVudSBleHRlbmRzIE1lbnUge1xuICBwcml2YXRlIF91c2VyOiBJQ3VycmVudFVzZXI7XG5cbiAgY29uc3RydWN0b3Iob3B0aW9uczogVXNlck1lbnUuSU9wdGlvbnMpIHtcbiAgICBzdXBlcihvcHRpb25zKTtcbiAgICB0aGlzLl91c2VyID0gb3B0aW9ucy51c2VyO1xuICAgIGNvbnN0IG5hbWUgPVxuICAgICAgdGhpcy5fdXNlci5kaXNwbGF5TmFtZSAhPT0gJycgPyB0aGlzLl91c2VyLmRpc3BsYXlOYW1lIDogdGhpcy5fdXNlci5uYW1lO1xuICAgIHRoaXMudGl0bGUubGFiZWwgPSB0aGlzLl91c2VyLmlzUmVhZHkgPyBuYW1lIDogJyc7XG4gICAgdGhpcy50aXRsZS5pY29uID0gY2FyZXREb3duSWNvbjtcbiAgICB0aGlzLnRpdGxlLmljb25DbGFzcyA9ICdqcC1Vc2VyTWVudS1jYXJldERvd25JY29uJztcbiAgICB0aGlzLl91c2VyLnJlYWR5LmNvbm5lY3QodGhpcy5fdXBkYXRlTGFiZWwpO1xuICAgIHRoaXMuX3VzZXIuY2hhbmdlZC5jb25uZWN0KHRoaXMuX3VwZGF0ZUxhYmVsKTtcbiAgfVxuXG4gIGRpc3Bvc2UoKSB7XG4gICAgdGhpcy5fdXNlci5yZWFkeS5kaXNjb25uZWN0KHRoaXMuX3VwZGF0ZUxhYmVsKTtcbiAgICB0aGlzLl91c2VyLmNoYW5nZWQuZGlzY29ubmVjdCh0aGlzLl91cGRhdGVMYWJlbCk7XG4gIH1cblxuICBwcml2YXRlIF91cGRhdGVMYWJlbCA9ICh1c2VyOiBJQ3VycmVudFVzZXIpID0+IHtcbiAgICBjb25zdCBuYW1lID0gdXNlci5kaXNwbGF5TmFtZSAhPT0gJycgPyB1c2VyLmRpc3BsYXlOYW1lIDogdXNlci5uYW1lO1xuICAgIHRoaXMudGl0bGUubGFiZWwgPSBuYW1lO1xuICAgIHRoaXMudXBkYXRlKCk7XG4gIH07XG59XG5cbi8qKlxuICogTmFtZXNwYWNlIG9mIHRoZSBVc2VyTWVudSBjbGFzcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBVc2VyTWVudSB7XG4gIC8qKlxuICAgKiBVc2VyIG1lbnUgb3B0aW9ucyBpbnRlcmZhY2VcbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMgZXh0ZW5kcyBNZW51LklPcHRpb25zIHtcbiAgICAvKipcbiAgICAgKiBDdXJyZW50IHVzZXIgb2JqZWN0LlxuICAgICAqL1xuICAgIHVzZXI6IElDdXJyZW50VXNlcjtcbiAgfVxufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBJU2lnbmFsLCBTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBVVUlEIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuXG5pbXBvcnQgeyBJQ3VycmVudFVzZXIsIElVc2VyLCBVU0VSIH0gZnJvbSAnLi90b2tlbnMnO1xuaW1wb3J0IHsgZ2V0QW5vbnltb3VzVXNlck5hbWUgfSBmcm9tICcuL3V0aWxzJztcblxuLyoqXG4gKiBEZWZhdWx0IHVzZXIgaW1wbGVtZW50YXRpb24uXG4gKi9cbmV4cG9ydCBjbGFzcyBVc2VyIGltcGxlbWVudHMgSUN1cnJlbnRVc2VyIHtcbiAgcHJpdmF0ZSBfdXNlcm5hbWU6IHN0cmluZztcbiAgcHJpdmF0ZSBfbmFtZTogc3RyaW5nO1xuICBwcml2YXRlIF9kaXNwbGF5TmFtZTogc3RyaW5nO1xuICBwcml2YXRlIF9pbml0aWFsczogc3RyaW5nO1xuICBwcml2YXRlIF9jb2xvcjogc3RyaW5nO1xuICBwcml2YXRlIF9hbm9ueW1vdXM6IGJvb2xlYW47XG4gIHByaXZhdGUgX2N1cnNvcj86IElVc2VyLkN1cnNvcjtcblxuICBwcml2YXRlIF9pc1JlYWR5ID0gZmFsc2U7XG4gIHByaXZhdGUgX3JlYWR5ID0gbmV3IFNpZ25hbDxVc2VyLCBib29sZWFuPih0aGlzKTtcbiAgcHJpdmF0ZSBfY2hhbmdlZCA9IG5ldyBTaWduYWw8VXNlciwgdm9pZD4odGhpcyk7XG5cbiAgLyoqXG4gICAqIENvbnN0cnVjdG9yIG9mIHRoZSBVc2VyIGNsYXNzLlxuICAgKi9cbiAgY29uc3RydWN0b3IoKSB7XG4gICAgdGhpcy5fZmV0Y2hVc2VyKCk7XG4gICAgdGhpcy5faXNSZWFkeSA9IHRydWU7XG4gICAgdGhpcy5fcmVhZHkuZW1pdCh0cnVlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVc2VyJ3MgdW5pcXVlIGlkZW50aWZpZXIuXG4gICAqL1xuICBnZXQgdXNlcm5hbWUoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5fdXNlcm5hbWU7XG4gIH1cblxuICAvKipcbiAgICogVXNlcidzIGZ1bGwgbmFtZS5cbiAgICovXG4gIGdldCBuYW1lKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHRoaXMuX25hbWU7XG4gIH1cblxuICAvKipcbiAgICogU2hvcnRlciB2ZXJzaW9uIG9mIHRoZSBuYW1lIGZvciBkaXNwbGF5aW5nIGl0IG9uIHRoZSBVSS5cbiAgICovXG4gIGdldCBkaXNwbGF5TmFtZSgpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9kaXNwbGF5TmFtZTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVc2VyJ3MgbmFtZSBpbml0aWFscy5cbiAgICovXG4gIGdldCBpbml0aWFscygpOiBzdHJpbmcge1xuICAgIHJldHVybiB0aGlzLl9pbml0aWFscztcbiAgfVxuXG4gIC8qKlxuICAgKiBVc2VyJ3MgY3Vyc29yIGNvbG9yIGFuZCBpY29uIGNvbG9yIGlmIGF2YXRhcl91cmwgaXMgdW5kZWZpbmVkXG4gICAqICh0aGVyZSBpcyBubyBpbWFnZSkuXG4gICAqL1xuICBnZXQgY29sb3IoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5fY29sb3I7XG4gIH1cbiAgc2V0IGNvbG9yKHZhbHVlOiBzdHJpbmcpIHtcbiAgICB0aGlzLl9jb2xvciA9IHZhbHVlO1xuICB9XG5cbiAgLyoqXG4gICAqIFdoZXRoZXIgdGhlIHVzZXIgaXMgYW5vbnltb3VzIG9yIG5vdC5cbiAgICpcbiAgICogTk9URTogSnVweXRlciBzZXJ2ZXIgZG9lc24ndCBoYW5kbGUgdXNlcidzIGlkZW50aXR5IHNvLCBieSBkZWZhdWx0IGV2ZXJ5IHVzZXJcbiAgICogaXMgYW5vbnltb3VzIHVubGVzcyBhIHRoaXJkLXBhcnR5IGV4dGVuc2lvbiBwcm92aWRlcyB0aGUgSUN1cnJlbnRVc2VyIHRva2VuIHJldHJpZXZpbmdcbiAgICogdGhlIHVzZXIgaWRlbnRpdHkgZnJvbSBhIHRoaXJkLXBhcnR5IGlkZW50aXR5IHByb3ZpZGVyIGFzIEdpdEh1YiwgR29vZ2xlLCBldGMuXG4gICAqL1xuICBnZXQgYW5vbnltb3VzKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiB0aGlzLl9hbm9ueW1vdXM7XG4gIH1cblxuICAvKipcbiAgICogVXNlcidzIGN1cnNvciBwb3NpdGlvbiBvbiB0aGUgZG9jdW1lbnQuXG4gICAqXG4gICAqIElmIHVuZGVmaW5lZCwgdGhlIHVzZXIgaXMgbm90IG9uIGEgZG9jdW1lbnQuXG4gICAqL1xuICBnZXQgY3Vyc29yKCk6IElVc2VyLkN1cnNvciB8IHVuZGVmaW5lZCB7XG4gICAgcmV0dXJuIHRoaXMuX2N1cnNvcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBXaGV0aGVyIHRoZSB1c2VyIGluZm9ybWF0aW9uIGlzIGxvYWRlZCBvciBub3QuXG4gICAqL1xuICBnZXQgaXNSZWFkeSgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5faXNSZWFkeTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTaWduYWwgZW1pdHRlZCB3aGVuIHRoZSB1c2VyJ3MgaW5mb3JtYXRpb24gaXMgcmVhZHkuXG4gICAqL1xuICBnZXQgcmVhZHkoKTogSVNpZ25hbDxJQ3VycmVudFVzZXIsIGJvb2xlYW4+IHtcbiAgICByZXR1cm4gdGhpcy5fcmVhZHk7XG4gIH1cblxuICAvKipcbiAgICogU2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgdXNlcidzIGluZm9ybWF0aW9uIGNoYW5nZXMuXG4gICAqL1xuICBnZXQgY2hhbmdlZCgpOiBJU2lnbmFsPElDdXJyZW50VXNlciwgdm9pZD4ge1xuICAgIHJldHVybiB0aGlzLl9jaGFuZ2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIENvbnZlbmllbmNlIG1ldGhvZCB0byBtb2RpZnkgdGhlIHVzZXIgYXMgYSBKU09OIG9iamVjdC5cbiAgICovXG4gIGZyb21KU09OKHVzZXI6IElVc2VyLlVzZXIpOiB2b2lkIHtcbiAgICB0aGlzLl91c2VybmFtZSA9IHVzZXIudXNlcm5hbWU7XG4gICAgdGhpcy5fbmFtZSA9IHVzZXIubmFtZTtcbiAgICB0aGlzLl9kaXNwbGF5TmFtZSA9IHVzZXIuZGlzcGxheU5hbWU7XG4gICAgdGhpcy5faW5pdGlhbHMgPSB1c2VyLmluaXRpYWxzO1xuICAgIHRoaXMuX2NvbG9yID0gdXNlci5jb2xvcjtcbiAgICB0aGlzLl9hbm9ueW1vdXMgPSB1c2VyLmFub255bW91cztcbiAgICB0aGlzLl9jdXJzb3IgPSB1c2VyLmN1cnNvcjtcbiAgICB0aGlzLl9zYXZlKCk7XG4gIH1cblxuICAvKipcbiAgICogQ29udmVuaWVuY2UgbWV0aG9kIHRvIGV4cG9ydCB0aGUgdXNlciBhcyBhIEpTT04gb2JqZWN0LlxuICAgKi9cbiAgdG9KU09OKCk6IElVc2VyLlVzZXIge1xuICAgIHJldHVybiB7XG4gICAgICB1c2VybmFtZTogdGhpcy5fdXNlcm5hbWUsXG4gICAgICBuYW1lOiB0aGlzLm5hbWUsXG4gICAgICBkaXNwbGF5TmFtZTogdGhpcy5fZGlzcGxheU5hbWUsXG4gICAgICBpbml0aWFsczogdGhpcy5faW5pdGlhbHMsXG4gICAgICBjb2xvcjogdGhpcy5fY29sb3IsXG4gICAgICBhbm9ueW1vdXM6IHRoaXMuX2Fub255bW91cyxcbiAgICAgIGN1cnNvcjogdGhpcy5fY3Vyc29yXG4gICAgfTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTYXZlcyB0aGUgdXNlciBpbmZvcm1hdGlvbiB0byBTdGF0ZURCLlxuICAgKi9cbiAgcHJpdmF0ZSBfc2F2ZSgpOiB2b2lkIHtcbiAgICBjb25zdCB7IGxvY2FsU3RvcmFnZSB9ID0gd2luZG93O1xuICAgIGxvY2FsU3RvcmFnZS5zZXRJdGVtKFVTRVIsIEpTT04uc3RyaW5naWZ5KHRoaXMudG9KU09OKCkpKTtcbiAgICB0aGlzLl9jaGFuZ2VkLmVtaXQoKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXRyaWV2ZXMgdGhlIHVzZXIgaW5mb3JtYXRpb24gZnJvbSBTdGF0ZURCLCBvciBpbml0aWFsaXplc1xuICAgKiB0aGUgdXNlciBhcyBhbm9ueW1vdXMgaWYgZG9lc24ndCBleGlzdHMuXG4gICAqL1xuICBwcml2YXRlIF9mZXRjaFVzZXIoKTogdm9pZCB7XG4gICAgLy8gUmVhZCB1c2VybmFtZSwgY29sb3IgYW5kIGluaXRpYWxzIGZyb20gVVJMXG4gICAgY29uc3QgdXJsUGFyYW1zID0gbmV3IFVSTFNlYXJjaFBhcmFtcyhsb2NhdGlvbi5zZWFyY2gpO1xuICAgIGxldCBuYW1lID0gdXJsUGFyYW1zLmdldCgndXNlcm5hbWUnKSB8fCAnJztcbiAgICBsZXQgY29sb3IgPSB1cmxQYXJhbXMuZ2V0KCd1c2VyY29sb3InKSB8fCAnJztcbiAgICBsZXQgaW5pdGlhbHMgPSB1cmxQYXJhbXMuZ2V0KCdpbml0aWFscycpIHx8ICcnO1xuXG4gICAgY29uc3QgeyBsb2NhbFN0b3JhZ2UgfSA9IHdpbmRvdztcbiAgICBjb25zdCBkYXRhID0gbG9jYWxTdG9yYWdlLmdldEl0ZW0oVVNFUik7XG4gICAgaWYgKGRhdGEgIT09IG51bGwpIHtcbiAgICAgIGNvbnN0IHVzZXIgPSBKU09OLnBhcnNlKGRhdGEpO1xuXG4gICAgICB0aGlzLl91c2VybmFtZSA9IHVzZXIudXNlcm5hbWUgYXMgc3RyaW5nO1xuICAgICAgdGhpcy5fbmFtZSA9IG5hbWUgIT09ICcnID8gbmFtZSA6ICh1c2VyLm5hbWUgYXMgc3RyaW5nKTtcbiAgICAgIHRoaXMuX2Rpc3BsYXlOYW1lID0gbmFtZSAhPT0gJycgPyBuYW1lIDogKHVzZXIuZGlzcGxheU5hbWUgYXMgc3RyaW5nKTtcbiAgICAgIHRoaXMuX2luaXRpYWxzID0gaW5pdGlhbHMgIT09ICcnID8gaW5pdGlhbHMgOiAodXNlci5pbml0aWFscyBhcyBzdHJpbmcpO1xuICAgICAgdGhpcy5fY29sb3IgPSBjb2xvciAhPT0gJycgPyAnIycgKyBjb2xvciA6ICh1c2VyLmNvbG9yIGFzIHN0cmluZyk7XG4gICAgICB0aGlzLl9hbm9ueW1vdXMgPSB1c2VyLmFub255bW91cyBhcyBib29sZWFuO1xuICAgICAgdGhpcy5fY3Vyc29yID0gKHVzZXIuY3Vyc29yIGFzIElVc2VyLkN1cnNvcikgfHwgdW5kZWZpbmVkO1xuXG4gICAgICBpZiAobmFtZSAhPT0gJycgfHwgY29sb3IgIT09ICcnKSB7XG4gICAgICAgIHRoaXMuX3NhdmUoKTtcbiAgICAgIH1cbiAgICB9IGVsc2Uge1xuICAgICAgLy8gR2V0IHJhbmRvbSB2YWx1ZXNcbiAgICAgIGNvbnN0IGFub255bW91c05hbWUgPSBnZXRBbm9ueW1vdXNVc2VyTmFtZSgpO1xuICAgICAgdGhpcy5fdXNlcm5hbWUgPSBVVUlELnV1aWQ0KCk7XG4gICAgICB0aGlzLl9uYW1lID0gbmFtZSAhPT0gJycgPyBuYW1lIDogJ0Fub255bW91cyAnICsgYW5vbnltb3VzTmFtZTtcbiAgICAgIHRoaXMuX2Rpc3BsYXlOYW1lID0gdGhpcy5fbmFtZTtcbiAgICAgIHRoaXMuX2luaXRpYWxzID1cbiAgICAgICAgaW5pdGlhbHMgIT09ICcnXG4gICAgICAgICAgPyBpbml0aWFsc1xuICAgICAgICAgIDogYEEke2Fub255bW91c05hbWUuc3Vic3RyaW5nKDAsIDEpLnRvTG9jYWxlVXBwZXJDYXNlKCl9YDtcbiAgICAgIHRoaXMuX2NvbG9yID0gY29sb3IgIT09ICcnID8gJyMnICsgY29sb3IgOiBQcml2YXRlLmdldFJhbmRvbUNvbG9yKCk7XG4gICAgICB0aGlzLl9hbm9ueW1vdXMgPSB0cnVlO1xuICAgICAgdGhpcy5fY3Vyc29yID0gdW5kZWZpbmVkO1xuICAgICAgdGhpcy5fc2F2ZSgpO1xuICAgIH1cbiAgfVxufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBtb2R1bGUtcHJpdmF0ZSBmdW5jdGlvbmFsaXR5LlxuICpcbiAqIE5vdGU6IFdlIGRvIG5vdCB3YW50IHRvIGV4cG9ydCB0aGlzIGZ1bmN0aW9uXG4gKiB0byBtb3ZlIGl0IHRvIGNzcyB2YXJpYWJsZXMgaW4gdGhlIFRoZW1lLlxuICovXG5uYW1lc3BhY2UgUHJpdmF0ZSB7XG4gIC8qKlxuICAgKiBQcmVkZWZpbmVkIGNvbG9ycyBmb3IgdXNlcnNcbiAgICovXG4gIGNvbnN0IHVzZXJDb2xvcnMgPSBbXG4gICAgJ3ZhcigtLWpwLWNvbGxhYm9yYXRvci1jb2xvcjEpJyxcbiAgICAndmFyKC0tanAtY29sbGFib3JhdG9yLWNvbG9yMiknLFxuICAgICd2YXIoLS1qcC1jb2xsYWJvcmF0b3ItY29sb3IzKScsXG4gICAgJ3ZhcigtLWpwLWNvbGxhYm9yYXRvci1jb2xvcjQpJyxcbiAgICAndmFyKC0tanAtY29sbGFib3JhdG9yLWNvbG9yNSknLFxuICAgICd2YXIoLS1qcC1jb2xsYWJvcmF0b3ItY29sb3I2KScsXG4gICAgJ3ZhcigtLWpwLWNvbGxhYm9yYXRvci1jb2xvcjcpJ1xuICBdO1xuXG4gIC8qKlxuICAgKiBHZXQgYSByYW5kb20gY29sb3IgZnJvbSB0aGUgbGlzdCBvZiBjb2xvcnMuXG4gICAqL1xuICBleHBvcnQgY29uc3QgZ2V0UmFuZG9tQ29sb3IgPSAoKTogc3RyaW5nID0+XG4gICAgdXNlckNvbG9yc1tNYXRoLmZsb29yKE1hdGgucmFuZG9tKCkgKiB1c2VyQ29sb3JzLmxlbmd0aCldO1xufVxuIiwiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuXG5pbXBvcnQgeyBNZW51IH0gZnJvbSAnQGx1bWluby93aWRnZXRzJztcbmltcG9ydCB7IElTaWduYWwgfSBmcm9tICdAbHVtaW5vL3NpZ25hbGluZyc7XG5pbXBvcnQgeyBUb2tlbiB9IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IEF3YXJlbmVzcyB9IGZyb20gJ3ktcHJvdG9jb2xzL2F3YXJlbmVzcyc7XG5cbi8qKlxuICogQW4gSUQgdG8gdHJhY2sgdGhlIHVzZXIgb24gU3RhdGVEQi5cbiAqL1xuZXhwb3J0IGNvbnN0IFVTRVIgPSAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbjp1c2VyREInO1xuXG4vKipcbiAqIEBleHBlcmltZW50YWxcbiAqIEBhbHBoYVxuICpcbiAqIFRoZSB1c2VyIHRva2VuLlxuICpcbiAqIE5PVEU6IFJlcXVpcmVyIHRoaXMgdG9rZW4gaW4geW91ciBleHRlbnNpb24gdG8gYWNjZXNzIHRoZVxuICogY3VycmVudCBjb25uZWN0ZWQgdXNlciBpbmZvcm1hdGlvbi5cbiAqL1xuZXhwb3J0IGNvbnN0IElDdXJyZW50VXNlciA9IG5ldyBUb2tlbjxJQ3VycmVudFVzZXI+KFxuICAnQGp1cHl0ZXJsYWIvY29sbGFib3JhdGlvbjpJQ3VycmVudFVzZXInXG4pO1xuXG4vKipcbiAqIFRoZSB1c2VyIG1lbnUgdG9rZW4uXG4gKlxuICogTk9URTogUmVxdWlyZSB0aGlzIHRva2VuIGluIHlvdXIgZXh0ZW5zaW9uIHRvIGFjY2VzcyB0aGUgdXNlciBtZW51XG4gKiAodG9wLXJpZ2h0IG1lbnUgaW4gSnVweXRlckxhYidzIGludGVyZmFjZSkuXG4gKi9cbmV4cG9ydCBjb25zdCBJVXNlck1lbnUgPSBuZXcgVG9rZW48SVVzZXJNZW51PihcbiAgJ0BqdXB5dGVybGFiL2NvbGxhYm9yYXRpb246SVVzZXJNZW51J1xuKTtcblxuLyoqXG4gKiBUaGUgZ2xvYmFsIGF3YXJlbmVzcyB0b2tlbi5cbiAqL1xuZXhwb3J0IGNvbnN0IElHbG9iYWxBd2FyZW5lc3MgPSBuZXcgVG9rZW48SUF3YXJlbmVzcz4oXG4gICdAanVweXRlcmxhYi9jb2xsYWJvcmF0aW9uOklHbG9iYWxBd2FyZW5lc3MnXG4pO1xuXG4vKipcbiAqIFRoZSBhd2FyZW5lc3MgaW50ZXJmYWNlLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElBd2FyZW5lc3MgZXh0ZW5kcyBBd2FyZW5lc3Mge31cblxuLyoqXG4gKiBAZXhwZXJpbWVudGFsXG4gKiBAYWxwaGFcbiAqXG4gKiBBbiBpbnRlcmZhY2UgZGVzY3JpYmluZyB0aGUgY3VycmVudCB1c2VyLlxuICovXG5leHBvcnQgaW50ZXJmYWNlIElDdXJyZW50VXNlciBleHRlbmRzIElVc2VyLlVzZXIge1xuICAvKipcbiAgICogV2hldGhlciB0aGUgdXNlciBpbmZvcm1hdGlvbiBpcyBsb2FkZWQgb3Igbm90LlxuICAgKi9cbiAgcmVhZG9ubHkgaXNSZWFkeTogYm9vbGVhbjtcblxuICAvKipcbiAgICogU2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgdXNlcidzIGluZm9ybWF0aW9uIGlzIHJlYWR5LlxuICAgKi9cbiAgcmVhZG9ubHkgcmVhZHk6IElTaWduYWw8SUN1cnJlbnRVc2VyLCBib29sZWFuPjtcblxuICAvKipcbiAgICogU2lnbmFsIGVtaXR0ZWQgd2hlbiB0aGUgdXNlcidzIGluZm9ybWF0aW9uIGNoYW5nZXMuXG4gICAqL1xuICByZWFkb25seSBjaGFuZ2VkOiBJU2lnbmFsPElDdXJyZW50VXNlciwgdm9pZD47XG5cbiAgLyoqXG4gICAqIENvbnZlbmllbmNlIG1ldGhvZCB0byBtb2RpZnkgdGhlIHVzZXIgYXMgYSBKU09OIG9iamVjdC5cbiAgICpcbiAgICogQGFyZ3VtZW50IHVzZXI6IHVzZXIgaW5mbyBhcyBKU09OIG9iamVjdC5cbiAgICovXG4gIGZyb21KU09OKHVzZXI6IElVc2VyLlVzZXIpOiB2b2lkO1xuXG4gIC8qKlxuICAgKiBDb252ZW5pZW5jZSBtZXRob2QgdG8gZXhwb3J0IHRoZSB1c2VyIGFzIGEgSlNPTiBvYmplY3QuXG4gICAqXG4gICAqIEByZXR1cm5zIHVzZXIgaW5mbyBhcyBKU09OIG9iamVjdC5cbiAgICovXG4gIHRvSlNPTigpOiBJVXNlci5Vc2VyO1xufVxuXG4vKipcbiAqIFRoZSB1c2VyIG5hbWVzcGFjZS5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBJVXNlciB7XG4gIC8qKlxuICAgKiBUaGUgdHlwZSBmb3IgdGhlIElVc2VyLlxuICAgKlxuICAgKiBDb252ZW5pZW5jZSBmb3IgdHJlYXRpbmcgdGhlIHVzZXIncyBpbmZvIGFzIGEgSlNPTiBvYmplY3QuXG4gICAqL1xuICBleHBvcnQgdHlwZSBVc2VyID0ge1xuICAgIC8qKlxuICAgICAqIFVzZXIncyB1bmlxdWUgaWRlbnRpZmllci5cbiAgICAgKi9cbiAgICByZWFkb25seSB1c2VybmFtZTogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVXNlcidzIGZ1bGwgbmFtZS5cbiAgICAgKi9cbiAgICByZWFkb25seSBuYW1lOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBTaG9ydGVyIHZlcnNpb24gb2YgdGhlIG5hbWUgZm9yIGRpc3BsYXlpbmcgaXQgb24gdGhlIFVJLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IGRpc3BsYXlOYW1lOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBVc2VyJ3MgbmFtZSBpbml0aWFscy5cbiAgICAgKi9cbiAgICByZWFkb25seSBpbml0aWFsczogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVXNlcidzIGN1cnNvciBjb2xvciBhbmQgaWNvbiBjb2xvciBpZiBhdmF0YXJfdXJsIGlzIHVuZGVmaW5lZFxuICAgICAqICh0aGVyZSBpcyBubyBpbWFnZSkuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY29sb3I6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFdoZXRoZXIgdGhlIHVzZXIgaXMgYW5vbnltb3VzIG9yIG5vdC5cbiAgICAgKlxuICAgICAqIE5PVEU6IEp1cHl0ZXIgc2VydmVyIGRvZXNuJ3QgaGFuZGxlIHVzZXIncyBpZGVudGl0eSBzbywgYnkgZGVmYXVsdCBldmVyeSB1c2VyXG4gICAgICogaXMgYW5vbnltb3VzIHVubGVzcyBhIHRoaXJkLXBhcnR5IGV4dGVuc2lvbiBwcm92aWRlcyB0aGUgSUN1cnJlbnRVc2VyIHRva2VuIHJldHJpZXZpbmdcbiAgICAgKiB0aGUgdXNlciBpZGVudGl0eSBmcm9tIGEgdGhpcmQtcGFydHkgaWRlbnRpdHkgcHJvdmlkZXIgYXMgR2l0SHViLCBHb29nbGUsIGV0Yy5cbiAgICAgKi9cbiAgICByZWFkb25seSBhbm9ueW1vdXM6IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBVc2VyJ3MgY3Vyc29yIHBvc2l0aW9uIG9uIHRoZSBkb2N1bWVudC5cbiAgICAgKlxuICAgICAqIElmIHVuZGVmaW5lZCwgdGhlIHVzZXIgaXMgbm90IG9uIGEgZG9jdW1lbnQuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY3Vyc29yPzogSVVzZXIuQ3Vyc29yO1xuXG4gICAgLyoqXG4gICAgICogVXNlcidzIGF2YXRhciB1cmwuXG4gICAgICogVGhlIHVybCB0byB0aGUgdXNlcidzIGltYWdlIGZvciB0aGUgaWNvbi5cbiAgICAgKi9cbiAgICByZWFkb25seSBhdmF0YXJfdXJsPzogc3RyaW5nO1xuICB9O1xuXG4gIGV4cG9ydCB0eXBlIEN1cnNvciA9IHtcbiAgICAvKipcbiAgICAgKiBEb2N1bWVudCB3aGVyZSB0aGUgdXNlciBpcyBjdXJyZW50bHkgZm9jdXNlZC5cbiAgICAgKi9cbiAgICBkb2N1bWVudDogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogQ2VsbCB3aGVyZSB0aGUgdXNlciBpcyBmb2N1c2VkLlxuICAgICAqXG4gICAgICogTk9URTogMCBmb3IgcGxhaW4gdGV4dCBmaWxlcy5cbiAgICAgKi9cbiAgICBjZWxsOiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBQb3NpdGlvbiBvZiB0aGUgY3Vyc29yIGluIHRoZSBjZWxsLlxuICAgICAqL1xuICAgIGluZGV4OiBudW1iZXI7XG4gIH07XG59XG5cbi8qKlxuICogQW4gaW50ZXJmYWNlIGRlc2NyaWJpbmcgdGhlIHVzZXIgbWVudS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJVXNlck1lbnUge1xuICAvKipcbiAgICogRGlzcG9zZSBvZiB0aGUgcmVzb3VyY2VzIGhlbGQgYnkgdGhlIG1lbnUuXG4gICAqL1xuICBkaXNwb3NlKCk6IHZvaWQ7XG5cbiAgLyoqXG4gICAqIFRlc3Qgd2hldGhlciB0aGUgd2lkZ2V0IGhhcyBiZWVuIGRpc3Bvc2VkLlxuICAgKi9cbiAgcmVhZG9ubHkgaXNEaXNwb3NlZDogYm9vbGVhbjtcblxuICAvKipcbiAgICogQSByZWFkLW9ubHkgYXJyYXkgb2YgdGhlIG1lbnUgaXRlbXMgaW4gdGhlIG1lbnUuXG4gICAqL1xuICByZWFkb25seSBpdGVtczogUmVhZG9ubHlBcnJheTxNZW51LklJdGVtPjtcblxuICAvKipcbiAgICogQWRkIGEgbWVudSBpdGVtIHRvIHRoZSBlbmQgb2YgdGhlIG1lbnUuXG4gICAqXG4gICAqIEBwYXJhbSBvcHRpb25zIC0gVGhlIG9wdGlvbnMgZm9yIGNyZWF0aW5nIHRoZSBtZW51IGl0ZW0uXG4gICAqXG4gICAqIEByZXR1cm5zIFRoZSBtZW51IGl0ZW0gYWRkZWQgdG8gdGhlIG1lbnUuXG4gICAqL1xuICBhZGRJdGVtKG9wdGlvbnM6IE1lbnUuSUl0ZW1PcHRpb25zKTogTWVudS5JSXRlbTtcblxuICAvKipcbiAgICogSW5zZXJ0IGEgbWVudSBpdGVtIGludG8gdGhlIG1lbnUgYXQgdGhlIHNwZWNpZmllZCBpbmRleC5cbiAgICpcbiAgICogQHBhcmFtIGluZGV4IC0gVGhlIGluZGV4IGF0IHdoaWNoIHRvIGluc2VydCB0aGUgaXRlbS5cbiAgICpcbiAgICogQHBhcmFtIG9wdGlvbnMgLSBUaGUgb3B0aW9ucyBmb3IgY3JlYXRpbmcgdGhlIG1lbnUgaXRlbS5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIG1lbnUgaXRlbSBhZGRlZCB0byB0aGUgbWVudS5cbiAgICpcbiAgICogIyMjIyBOb3Rlc1xuICAgKiBUaGUgaW5kZXggd2lsbCBiZSBjbGFtcGVkIHRvIHRoZSBib3VuZHMgb2YgdGhlIGl0ZW1zLlxuICAgKi9cbiAgaW5zZXJ0SXRlbShpbmRleDogbnVtYmVyLCBvcHRpb25zOiBNZW51LklJdGVtT3B0aW9ucyk6IE1lbnUuSUl0ZW07XG5cbiAgLyoqXG4gICAqIFJlbW92ZSBhbiBpdGVtIGZyb20gdGhlIG1lbnUuXG4gICAqXG4gICAqIEBwYXJhbSBpdGVtIC0gVGhlIGl0ZW0gdG8gcmVtb3ZlIGZyb20gdGhlIG1lbnUuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBpcyBhIG5vLW9wIGlmIHRoZSBpdGVtIGlzIG5vdCBpbiB0aGUgbWVudS5cbiAgICovXG4gIHJlbW92ZUl0ZW0oaXRlbTogTWVudS5JSXRlbSk6IHZvaWQ7XG59XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IFJlYWN0V2lkZ2V0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvYXBwdXRpbHMnO1xuXG5pbXBvcnQgKiBhcyBSZWFjdCBmcm9tICdyZWFjdCc7XG5cbmltcG9ydCB7IElDdXJyZW50VXNlciwgSVVzZXIgfSBmcm9tICcuL3Rva2Vucyc7XG5pbXBvcnQgeyBVc2VySWNvbkNvbXBvbmVudCB9IGZyb20gJy4vY29tcG9uZW50cyc7XG5pbXBvcnQgeyBQYW5lbCB9IGZyb20gJ0BsdW1pbm8vd2lkZ2V0cyc7XG5cbmV4cG9ydCBjbGFzcyBVc2VySW5mb1BhbmVsIGV4dGVuZHMgUGFuZWwge1xuICBwcml2YXRlIF9wcm9maWxlOiBJQ3VycmVudFVzZXI7XG4gIHByaXZhdGUgX2JvZHk6IFVzZXJJbmZvQm9keTtcblxuICBjb25zdHJ1Y3Rvcih1c2VyOiBJQ3VycmVudFVzZXIpIHtcbiAgICBzdXBlcih7fSk7XG4gICAgdGhpcy5hZGRDbGFzcygnanAtVXNlckluZm9QYW5lbCcpO1xuXG4gICAgdGhpcy5fcHJvZmlsZSA9IHVzZXI7XG5cbiAgICBpZiAodGhpcy5fcHJvZmlsZS5pc1JlYWR5KSB7XG4gICAgICB0aGlzLl9ib2R5ID0gbmV3IFVzZXJJbmZvQm9keSh1c2VyLnRvSlNPTigpKTtcbiAgICAgIHRoaXMuYWRkV2lkZ2V0KHRoaXMuX2JvZHkpO1xuICAgICAgdGhpcy51cGRhdGUoKTtcbiAgICB9IGVsc2Uge1xuICAgICAgdGhpcy5fcHJvZmlsZS5yZWFkeS5jb25uZWN0KHVzZXIgPT4ge1xuICAgICAgICB0aGlzLl9ib2R5ID0gbmV3IFVzZXJJbmZvQm9keSh1c2VyLnRvSlNPTigpKTtcbiAgICAgICAgdGhpcy5hZGRXaWRnZXQodGhpcy5fYm9keSk7XG4gICAgICAgIHRoaXMudXBkYXRlKCk7XG4gICAgICB9KTtcbiAgICB9XG4gIH1cbn1cblxuLyoqXG4gKiBBIFNldHRpbmdzV2lkZ2V0IGZvciB0aGUgdXNlci5cbiAqL1xuZXhwb3J0IGNsYXNzIFVzZXJJbmZvQm9keSBleHRlbmRzIFJlYWN0V2lkZ2V0IHtcbiAgcHJpdmF0ZSBfdXNlcjogSVVzZXIuVXNlcjtcblxuICAvKipcbiAgICogQ29uc3RydWN0cyBhIG5ldyBzZXR0aW5ncyB3aWRnZXQuXG4gICAqL1xuICBjb25zdHJ1Y3Rvcih1c2VyOiBJVXNlci5Vc2VyKSB7XG4gICAgc3VwZXIoKTtcbiAgICB0aGlzLl91c2VyID0gdXNlcjtcbiAgfVxuXG4gIGdldCB1c2VyKCk6IElVc2VyLlVzZXIge1xuICAgIHJldHVybiB0aGlzLl91c2VyO1xuICB9XG5cbiAgc2V0IHVzZXIodXNlcjogSVVzZXIuVXNlcikge1xuICAgIHRoaXMuX3VzZXIgPSB1c2VyO1xuICAgIHRoaXMudXBkYXRlKCk7XG4gIH1cblxuICByZW5kZXIoKTogSlNYLkVsZW1lbnQge1xuICAgIHJldHVybiA8VXNlckljb25Db21wb25lbnQgdXNlcj17dGhpcy5fdXNlcn0gLz47XG4gIH1cbn1cbiIsIi8vIENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxuLy8gRGlzdHJpYnV0ZWQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBNb2RpZmllZCBCU0QgTGljZW5zZS5cblxuaW1wb3J0IHsgVVJMRXh0IH0gZnJvbSAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzJztcbmltcG9ydCB7IFNlcnZlckNvbm5lY3Rpb24gfSBmcm9tICdAanVweXRlcmxhYi9zZXJ2aWNlcyc7XG5pbXBvcnQgeyBJVXNlciB9IGZyb20gJy4vdG9rZW5zJztcblxuLyoqXG4gKiBDYWxsIHRoZSBBUEkgZXh0ZW5zaW9uXG4gKlxuICogQHBhcmFtIGVuZFBvaW50IEFQSSBSRVNUIGVuZCBwb2ludCBmb3IgdGhlIGV4dGVuc2lvblxuICogQHBhcmFtIGluaXQgSW5pdGlhbCB2YWx1ZXMgZm9yIHRoZSByZXF1ZXN0XG4gKiBAcmV0dXJucyBUaGUgcmVzcG9uc2UgYm9keSBpbnRlcnByZXRlZCBhcyBKU09OXG4gKi9cbmV4cG9ydCBhc3luYyBmdW5jdGlvbiByZXF1ZXN0QVBJPFQ+KFxuICBlbmRQb2ludCA9ICcnLFxuICBpbml0OiBSZXF1ZXN0SW5pdCA9IHt9XG4pOiBQcm9taXNlPFQ+IHtcbiAgY29uc3Qgc2V0dGluZ3MgPSBTZXJ2ZXJDb25uZWN0aW9uLm1ha2VTZXR0aW5ncygpO1xuICBjb25zdCByZXF1ZXN0VXJsID0gVVJMRXh0LmpvaW4oc2V0dGluZ3MuYmFzZVVybCwgZW5kUG9pbnQpO1xuXG4gIGxldCByZXNwb25zZTogUmVzcG9uc2U7XG4gIHRyeSB7XG4gICAgcmVzcG9uc2UgPSBhd2FpdCBTZXJ2ZXJDb25uZWN0aW9uLm1ha2VSZXF1ZXN0KHJlcXVlc3RVcmwsIGluaXQsIHNldHRpbmdzKTtcbiAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICB0aHJvdyBuZXcgU2VydmVyQ29ubmVjdGlvbi5OZXR3b3JrRXJyb3IoZXJyb3IpO1xuICB9XG5cbiAgbGV0IGRhdGE6IGFueSA9IGF3YWl0IHJlc3BvbnNlLnRleHQoKTtcblxuICBpZiAoZGF0YS5sZW5ndGggPiAwKSB7XG4gICAgdHJ5IHtcbiAgICAgIGRhdGEgPSBKU09OLnBhcnNlKGRhdGEpO1xuICAgIH0gY2F0Y2ggKGVycm9yKSB7XG4gICAgICBjb25zb2xlLmxvZygnTm90IGEgSlNPTiByZXNwb25zZSBib2R5LicsIHJlc3BvbnNlKTtcbiAgICB9XG4gIH1cblxuICBpZiAoIXJlc3BvbnNlLm9rKSB7XG4gICAgdGhyb3cgbmV3IFNlcnZlckNvbm5lY3Rpb24uUmVzcG9uc2VFcnJvcihyZXNwb25zZSwgZGF0YS5tZXNzYWdlIHx8IGRhdGEpO1xuICB9XG5cbiAgcmV0dXJuIGRhdGE7XG59XG5cbi8vIEZyb20gaHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTW9vbnNfb2ZfSnVwaXRlclxuZXhwb3J0IGNvbnN0IG1vb25zT2ZKdXB5dGVyID0gW1xuICAnTWV0aXMnLFxuICAnQWRyYXN0ZWEnLFxuICAnQW1hbHRoZWEnLFxuICAnVGhlYmUnLFxuICAnSW8nLFxuICAnRXVyb3BhJyxcbiAgJ0dhbnltZWRlJyxcbiAgJ0NhbGxpc3RvJyxcbiAgJ1RoZW1pc3RvJyxcbiAgJ0xlZGEnLFxuICAnRXJzYScsXG4gICdQYW5kaWEnLFxuICAnSGltYWxpYScsXG4gICdMeXNpdGhlYScsXG4gICdFbGFyYScsXG4gICdEaWEnLFxuICAnQ2FycG8nLFxuICAnVmFsZXR1ZG8nLFxuICAnRXVwb3JpZScsXG4gICdFdXBoZW1lJyxcbiAgLy8gJ1MvMjAwMyBKIDE4JyxcbiAgLy8gJ1MvMjAxMCBKIDInLFxuICAnSGVsaWtlJyxcbiAgLy8gJ1MvMjAwMyBKIDE2JyxcbiAgLy8gJ1MvMjAwMyBKIDInLFxuICAnRXVhbnRoZScsXG4gIC8vICdTLzIwMTcgSiA3JyxcbiAgJ0hlcm1pcHBlJyxcbiAgJ1ByYXhpZGlrZScsXG4gICdUaHlvbmUnLFxuICAnVGhlbHhpbm9lJyxcbiAgLy8gJ1MvMjAxNyBKIDMnLFxuICAnQW5hbmtlJyxcbiAgJ01uZW1lJyxcbiAgLy8gJ1MvMjAxNiBKIDEnLFxuICAnT3J0aG9zaWUnLFxuICAnSGFycGFseWtlJyxcbiAgJ0lvY2FzdGUnLFxuICAvLyAnUy8yMDE3IEogOScsXG4gIC8vICdTLzIwMDMgSiAxMicsXG4gIC8vICdTLzIwMDMgSiA0JyxcbiAgJ0VyaW5vbWUnLFxuICAnQWl0bmUnLFxuICAnSGVyc2UnLFxuICAnVGF5Z2V0ZScsXG4gIC8vICdTLzIwMTcgSiAyJyxcbiAgLy8gJ1MvMjAxNyBKIDYnLFxuICAnRXVrZWxhZGUnLFxuICAnQ2FybWUnLFxuICAvLyAnUy8yMDAzIEogMTknLFxuICAnSXNvbm9lJyxcbiAgLy8gJ1MvMjAwMyBKIDEwJyxcbiAgJ0F1dG9ub2UnLFxuICAnUGhpbG9waHJvc3luZScsXG4gICdDeWxsZW5lJyxcbiAgJ1Bhc2l0aGVlJyxcbiAgLy8gJ1MvMjAxMCBKIDEnLFxuICAnUGFzaXBoYWUnLFxuICAnU3BvbmRlJyxcbiAgLy8gJ1MvMjAxNyBKIDgnLFxuICAnRXVyeWRvbWUnLFxuICAvLyAnUy8yMDE3IEogNScsXG4gICdLYWx5a2UnLFxuICAnSGVnZW1vbmUnLFxuICAnS2FsZScsXG4gICdLYWxsaWNob3JlJyxcbiAgLy8gJ1MvMjAxMSBKIDEnLFxuICAvLyAnUy8yMDE3IEogMScsXG4gICdDaGFsZGVuZScsXG4gICdBcmNoZScsXG4gICdFaXJlbmUnLFxuICAnS29yZScsXG4gIC8vICdTLzIwMTEgSiAyJyxcbiAgLy8gJ1MvMjAwMyBKIDknLFxuICAnTWVnYWNsaXRlJyxcbiAgJ0FvZWRlJyxcbiAgLy8gJ1MvMjAwMyBKIDIzJyxcbiAgJ0NhbGxpcnJob2UnLFxuICAnU2lub3BlJ1xuXTtcblxuLyoqXG4gKiBHZXQgYSByYW5kb20gdXNlci1uYW1lIGJhc2VkIG9uIHRoZSBtb29ucyBvZiBKdXB5dGVyLlxuICogVGhpcyBmdW5jdGlvbiByZXR1cm5zIG5hbWVzIGxpa2UgXCJBbm9ueW1vdXMgSW9cIiBvciBcIkFub255bW91cyBNZXRpc1wiLlxuICovXG5leHBvcnQgY29uc3QgZ2V0QW5vbnltb3VzVXNlck5hbWUgPSAoKTogc3RyaW5nID0+XG4gIG1vb25zT2ZKdXB5dGVyW01hdGguZmxvb3IoTWF0aC5yYW5kb20oKSAqIG1vb25zT2ZKdXB5dGVyLmxlbmd0aCldO1xuXG4vKipcbiAqIEdsb2JhbCBhd2FyZW5lc3MgZm9yIEp1cHl0ZXJMYWIgc2NvcHBlZCBzaGFyZWQgZGF0YS5cbiAqL1xuZXhwb3J0IGludGVyZmFjZSBJQ29sbGFib3JhdG9yQXdhcmVuZXNzIHtcbiAgLyoqXG4gICAqIFRoZSBVc2VyIG93bmluZyB0aGVzZXMgZGF0YS5cbiAgICovXG4gIHVzZXI6IElVc2VyLlVzZXI7XG5cbiAgLyoqXG4gICAqIFRoZSBjdXJyZW50IGZpbGUvY29udGV4dCB0aGUgdXNlciBpcyB3b3JraW5nIG9uLlxuICAgKi9cbiAgY3VycmVudD86IHN0cmluZztcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==