"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_lsp-extension_lib_index_js"],{

/***/ "../../packages/lsp-extension/lib/index.js":
/*!*************************************************!*\
  !*** ../../packages/lsp-extension/lib/index.js ***!
  \*************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RunningLanguageServers": () => (/* binding */ RunningLanguageServers),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/lsp */ "webpack/sharing/consume/default/@jupyterlab/lsp/@jupyterlab/lsp");
/* harmony import */ var _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/running */ "webpack/sharing/consume/default/@jupyterlab/running/@jupyterlab/running");
/* harmony import */ var _jupyterlab_running__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _renderer__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./renderer */ "../../packages/lsp-extension/lib/renderer.js");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 * @packageDocumentation
 * @module lsp-extension
 */







const plugin = {
    activate,
    id: '@jupyterlab/lsp-extension:plugin',
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_2__.ISettingRegistry, _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_3__.ITranslator],
    optional: [_jupyterlab_running__WEBPACK_IMPORTED_MODULE_1__.IRunningSessionManagers, _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.IFormComponentRegistry],
    provides: _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.ILSPDocumentConnectionManager,
    autoStart: true
};
const featurePlugin = {
    id: '@jupyterlab/lsp-extension:feature',
    activate: () => new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.FeatureManager(),
    provides: _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.ILSPFeatureManager,
    autoStart: true
};
const codeExtractorManagerPlugin = {
    id: _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.ILSPCodeExtractorsManager.name,
    activate: app => {
        const extractorManager = new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.CodeExtractorsManager();
        const markdownCellExtractor = new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.TextForeignCodeExtractor({
            language: 'markdown',
            isStandalone: false,
            file_extension: 'md',
            cellType: ['markdown']
        });
        extractorManager.register(markdownCellExtractor, null);
        const rawCellExtractor = new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.TextForeignCodeExtractor({
            language: 'text',
            isStandalone: false,
            file_extension: 'txt',
            cellType: ['raw']
        });
        extractorManager.register(rawCellExtractor, null);
        return extractorManager;
    },
    provides: _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.ILSPCodeExtractorsManager,
    autoStart: true
};
/**
 * Activate the lsp plugin.
 */
function activate(app, settingRegistry, translator, runningSessionManagers, settingRendererRegistry) {
    const LANGUAGE_SERVERS = 'languageServers';
    const languageServerManager = new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.LanguageServerManager({});
    const connectionManager = new _jupyterlab_lsp__WEBPACK_IMPORTED_MODULE_0__.DocumentConnectionManager({
        languageServerManager
    });
    const updateOptions = (settings) => {
        const options = settings.composite;
        const languageServerSettings = (options.languageServers ||
            {});
        connectionManager.initialConfigurations = languageServerSettings;
        // TODO: if priorities changed reset connections
        connectionManager.updateConfiguration(languageServerSettings);
        connectionManager.updateServerConfigurations(languageServerSettings);
        connectionManager.updateLogging(options.logAllCommunication, options.setTrace);
    };
    settingRegistry.transform(plugin.id, {
        fetch: plugin => {
            const schema = plugin.schema.properties;
            const defaultValue = {};
            languageServerManager.sessions.forEach((_, key) => {
                defaultValue[key] = { rank: 50, configuration: {} };
            });
            schema[LANGUAGE_SERVERS]['default'] = defaultValue;
            return plugin;
        },
        compose: plugin => {
            const properties = plugin.schema.properties;
            const user = plugin.data.user;
            const serverDefaultSettings = properties[LANGUAGE_SERVERS]['default'];
            const serverUserSettings = user[LANGUAGE_SERVERS];
            let serverComposite = Object.assign({}, serverDefaultSettings);
            if (serverUserSettings) {
                serverComposite = Object.assign(Object.assign({}, serverComposite), serverUserSettings);
            }
            const composite = {
                [LANGUAGE_SERVERS]: serverComposite
            };
            Object.entries(properties).forEach(([key, value]) => {
                if (key !== LANGUAGE_SERVERS) {
                    if (key in user) {
                        composite[key] = user[key];
                    }
                    else {
                        composite[key] = value.default;
                    }
                }
            });
            plugin.data.composite = composite;
            return plugin;
        }
    });
    languageServerManager.sessionsChanged.connect(async () => {
        await settingRegistry.reload(plugin.id);
    });
    settingRegistry
        .load(plugin.id)
        .then(settings => {
        updateOptions(settings);
        settings.changed.connect(() => {
            updateOptions(settings);
        });
    })
        .catch((reason) => {
        console.error(reason.message);
    });
    // Add a sessions manager if the running extension is available
    if (runningSessionManagers) {
        addRunningSessionManager(runningSessionManagers, connectionManager, translator);
    }
    if (settingRendererRegistry) {
        settingRendererRegistry.addRenderer(LANGUAGE_SERVERS, (props) => {
            return (0,_renderer__WEBPACK_IMPORTED_MODULE_6__.renderServerSetting)(props, translator);
        });
    }
    return connectionManager;
}
class RunningLanguageServers {
    constructor(connection, manager) {
        this._connection = connection;
        this._manager = manager;
    }
    /**
     * This is no-op because we do not do anything on server click event
     */
    open() {
        /** no-op */
    }
    icon() {
        return _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_4__.pythonIcon;
    }
    label() {
        var _a, _b;
        return `${(_a = this._connection.serverIdentifier) !== null && _a !== void 0 ? _a : ''} (${(_b = this._connection.serverLanguage) !== null && _b !== void 0 ? _b : ''})`;
    }
    shutdown() {
        for (const [key, value] of this._manager.connections.entries()) {
            if (value === this._connection) {
                const document = this._manager.documents.get(key);
                this._manager.unregisterDocument(document);
            }
        }
        this._manager.disconnect(this._connection.serverIdentifier);
    }
}
/**
 * Add the running terminal manager to the running panel.
 */
function addRunningSessionManager(managers, lsManager, translator) {
    const trans = translator.load('jupyterlab');
    const signal = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_5__.Signal(lsManager);
    lsManager.connected.connect(() => signal.emit(lsManager));
    lsManager.disconnected.connect(() => signal.emit(lsManager));
    lsManager.closed.connect(() => signal.emit(lsManager));
    lsManager.documentsChanged.connect(() => signal.emit(lsManager));
    let currentRunning = [];
    managers.add({
        name: trans.__('Language servers'),
        running: () => {
            const connections = new Set([...lsManager.connections.values()]);
            currentRunning = [...connections].map(conn => new RunningLanguageServers(conn, lsManager));
            return currentRunning;
        },
        shutdownAll: () => {
            currentRunning.forEach(item => {
                item.shutdown();
            });
        },
        refreshRunning: () => {
            return void 0;
        },
        runningChanged: signal,
        shutdownLabel: trans.__('Shut Down'),
        shutdownAllLabel: trans.__('Shut Down All'),
        shutdownAllConfirmationText: trans.__('Are you sure you want to permanently shut down all running language servers?')
    });
}
/**
 * Export the plugin as default.
 */
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([plugin, featurePlugin, codeExtractorManagerPlugin]);


/***/ }),

/***/ "../../packages/lsp-extension/lib/renderer.js":
/*!****************************************************!*\
  !*** ../../packages/lsp-extension/lib/renderer.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "renderServerSetting": () => (/* binding */ renderServerSetting)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/polling */ "webpack/sharing/consume/default/@lumino/polling/@lumino/polling");
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_polling__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
var __rest = (undefined && undefined.__rest) || function (s, e) {
    var t = {};
    for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p) && e.indexOf(p) < 0)
        t[p] = s[p];
    if (s != null && typeof Object.getOwnPropertySymbols === "function")
        for (var i = 0, p = Object.getOwnPropertySymbols(s); i < p.length; i++) {
            if (e.indexOf(p[i]) < 0 && Object.prototype.propertyIsEnumerable.call(s, p[i]))
                t[p[i]] = s[p[i]];
        }
    return t;
};




const SETTING_NAME = 'languageServers';
const SERVER_SETTINGS = 'configuration';
/**
 * The React component of the setting field
 */
function BuildSettingForm(props) {
    const _a = props.schema, _b = SERVER_SETTINGS, serverSettingsSchema = _a[_b], otherSettingsSchema = __rest(_a, [typeof _b === "symbol" ? _b : _b + ""]);
    const _c = props.settings, _d = SERVER_SETTINGS, serverSettings = _c[_d], { serverName } = _c, otherSettings = __rest(_c, [typeof _d === "symbol" ? _d : _d + "", "serverName"]);
    const [currentServerName, setCurrentServerName] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(serverName);
    /**
     * Callback on server name field change event
     */
    const onServerNameChange = (e) => {
        props.updateSetting
            .invoke(props.serverHash, {
            serverName: e.target.value
        })
            .catch(console.error);
        setCurrentServerName(e.target.value);
    };
    const serverSettingWithType = {};
    Object.entries(serverSettings).forEach(([key, value]) => {
        const newProps = {
            property: key,
            type: typeof value,
            value
        };
        serverSettingWithType[_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.UUID.uuid4()] = newProps;
    });
    const [propertyMap, setPropertyMap] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(serverSettingWithType);
    const defaultOtherSettings = {};
    Object.entries(otherSettingsSchema).forEach(([key, value]) => {
        if (key in otherSettings) {
            defaultOtherSettings[key] = otherSettings[key];
        }
        else {
            defaultOtherSettings[key] = value['default'];
        }
    });
    const [otherSettingsComposite, setOtherSettingsComposite] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(defaultOtherSettings);
    /**
     * Callback on additional setting field change event
     */
    const onOtherSettingsChange = (property, value, type) => {
        let settingValue = value;
        if (type === 'number') {
            settingValue = parseFloat(value);
        }
        const newProps = Object.assign(Object.assign({}, otherSettingsComposite), { [property]: settingValue });
        props.updateSetting.invoke(props.serverHash, newProps).catch(console.error);
        setOtherSettingsComposite(newProps);
    };
    /**
     * Callback on `Add property` button click event.
     */
    const addProperty = () => {
        const hash = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.UUID.uuid4();
        const newMap = Object.assign(Object.assign({}, propertyMap), { [hash]: { property: '', type: 'string', value: '' } });
        const payload = {};
        Object.values(newMap).forEach(value => {
            payload[value.property] = value.value;
        });
        props.updateSetting
            .invoke(props.serverHash, {
            [SERVER_SETTINGS]: payload
        })
            .catch(console.error);
        setPropertyMap(newMap);
    };
    /**
     * Callback on `Remove property` button click event.
     */
    const removeProperty = (entryHash) => {
        const newMap = {};
        Object.entries(propertyMap).forEach(([hash, value]) => {
            if (hash !== entryHash) {
                newMap[hash] = value;
            }
            const payload = {};
            Object.values(newMap).forEach(value => {
                payload[value.property] = value.value;
            });
            props.updateSetting
                .invoke(props.serverHash, {
                [SERVER_SETTINGS]: payload
            })
                .catch(console.error);
            setPropertyMap(newMap);
        });
    };
    /**
     * Save setting to the setting registry on field change event.
     */
    const setProperty = (hash, property) => {
        if (hash in propertyMap) {
            const newMap = Object.assign(Object.assign({}, propertyMap), { [hash]: property });
            const payload = {};
            Object.values(newMap).forEach(value => {
                payload[value.property] = value.value;
            });
            setPropertyMap(newMap);
            props.updateSetting
                .invoke(props.serverHash, {
                [SERVER_SETTINGS]: payload
            })
                .catch(console.error);
        }
    };
    const debouncedSetProperty = new _lumino_polling__WEBPACK_IMPORTED_MODULE_2__.Debouncer(setProperty);
    return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "array-item" },
        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "form-group " },
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-FormGroup-content" },
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-objectFieldWrapper" },
                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("fieldset", null,
                        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "form-group small-field" },
                            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-modifiedIndicator jp-errorIndicator" }),
                            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-FormGroup-content" },
                                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("h3", { className: "jp-FormGroup-fieldLabel jp-FormGroup-contentItem" }, props.trans.__('Server name:')),
                                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-inputFieldWrapper jp-FormGroup-contentItem" },
                                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("input", { className: "form-control", type: "text", required: true, value: currentServerName, onChange: e => {
                                            onServerNameChange(e);
                                        } })),
                                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "validationErrors" },
                                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", null,
                                        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("ul", { className: "error-detail bs-callout bs-callout-info" },
                                            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("li", { className: "text-danger" }, props.trans.__('is a required property'))))))),
                        Object.entries(otherSettingsSchema).map(([property, value], idx) => {
                            return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { key: `${idx}-${property}`, className: "form-group small-field" },
                                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-FormGroup-content" },
                                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("h3", { className: "jp-FormGroup-fieldLabel jp-FormGroup-contentItem" }, value.title),
                                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-inputFieldWrapper jp-FormGroup-contentItem" },
                                        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("input", { className: "form-control", placeholder: "", type: value.type, value: otherSettingsComposite[property], onChange: e => onOtherSettingsChange(property, e.target.value, value.type) })),
                                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-FormGroup-description" }, value.description),
                                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "validationErrors" }))));
                        }),
                        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("fieldset", null,
                            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("legend", null, serverSettingsSchema['title']),
                            Object.entries(propertyMap).map(([hash, property]) => {
                                return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(PropertyFrom, { key: hash, hash: hash, property: property, removeProperty: removeProperty, setProperty: debouncedSetProperty }));
                            }),
                            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("span", null, serverSettingsSchema['description'])))))),
        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-ArrayOperations" },
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("button", { className: "jp-mod-styled jp-mod-reject", onClick: addProperty }, props.trans.__('Add property')),
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("button", { className: "jp-mod-styled jp-mod-warn jp-FormGroup-removeButton", onClick: () => props.removeSetting(props.serverHash) }, props.trans.__('Remove server')))));
}
function PropertyFrom(props) {
    const [state, setState] = (0,react__WEBPACK_IMPORTED_MODULE_3__.useState)(Object.assign({}, props.property));
    const TYPE_MAP = { string: 'text', number: 'number', boolean: 'checkbox' };
    const removeItem = () => {
        props.removeProperty(props.hash);
    };
    const changeName = (newName) => {
        const newState = Object.assign(Object.assign({}, state), { property: newName });
        props.setProperty.invoke(props.hash, newState).catch(console.error);
        setState(newState);
    };
    const changeValue = (newValue, type) => {
        let value = newValue;
        if (type === 'number') {
            value = parseFloat(newValue);
        }
        const newState = Object.assign(Object.assign({}, state), { value });
        props.setProperty.invoke(props.hash, newState).catch(console.error);
        setState(newState);
    };
    const changeType = (newType) => {
        let value;
        if (newType === 'boolean') {
            value = false;
        }
        else if (newType === 'number') {
            value = 0;
        }
        else {
            value = '';
        }
        const newState = Object.assign(Object.assign({}, state), { type: newType, value });
        setState(newState);
        props.setProperty.invoke(props.hash, newState).catch(console.error);
    };
    return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { key: props.hash, className: "form-group small-field" },
        react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "jp-FormGroup-content jp-LSPExtension-FormGroup-content" },
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("input", { className: "form-control", type: "text", required: true, placeholder: 'Property name', value: state.property, onChange: e => {
                    changeName(e.target.value);
                } }),
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("select", { className: "form-control", value: state.type, onChange: e => changeType(e.target.value) },
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("option", { value: "string" }, "String"),
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("option", { value: "number" }, "Number"),
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("option", { value: "boolean" }, "Boolean")),
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("input", { className: "form-control", type: TYPE_MAP[state.type], required: false, placeholder: 'Property value', value: state.type !== 'boolean' ? state.value : undefined, checked: state.type === 'boolean' ? state.value : undefined, onChange: state.type !== 'boolean'
                    ? e => changeValue(e.target.value, state.type)
                    : e => changeValue(e.target.checked, state.type) }),
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("button", { className: "jp-mod-minimal jp-Button", onClick: removeItem },
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.closeIcon.react, null)))));
}
/**
 * React setting component
 */
class SettingRenderer extends (react__WEBPACK_IMPORTED_MODULE_3___default().Component) {
    constructor(props) {
        super(props);
        /**
         * Remove a setting item by its hash
         *
         * @param hash - hash of the item to be removed.
         */
        this.removeSetting = (hash) => {
            if (hash in this.state.items) {
                const items = {};
                for (const key in this.state.items) {
                    if (key !== hash) {
                        items[key] = this.state.items[key];
                    }
                }
                this.setState(old => {
                    return Object.assign(Object.assign({}, old), { items });
                }, () => {
                    this.saveServerSetting();
                });
            }
        };
        /**
         * Update a setting item by its hash
         *
         * @param hash - hash of the item to be updated.
         * @param newSetting - new setting value.
         */
        this.updateSetting = (hash, newSetting) => {
            if (hash in this.state.items) {
                const items = {};
                for (const key in this.state.items) {
                    if (key === hash) {
                        items[key] = Object.assign(Object.assign({}, this.state.items[key]), newSetting);
                    }
                    else {
                        items[key] = this.state.items[key];
                    }
                }
                this.setState(old => {
                    return Object.assign(Object.assign({}, old), { items });
                }, () => {
                    this.saveServerSetting();
                });
            }
        };
        /**
         * Add setting item to the setting component.
         */
        this.addServerSetting = () => {
            let index = 0;
            let key = 'newKey';
            while (Object.values(this.state.items)
                .map(val => val.serverName)
                .includes(key)) {
                index += 1;
                key = `newKey-${index}`;
            }
            this.setState(old => (Object.assign(Object.assign({}, old), { items: Object.assign(Object.assign({}, old.items), { [_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.UUID.uuid4()]: Object.assign(Object.assign({}, this._defaultSetting), { serverName: key }) }) })), () => {
                this.saveServerSetting();
            });
        };
        /**
         * Save the value of setting items to the setting registry.
         */
        this.saveServerSetting = () => {
            const settings = {};
            Object.values(this.state.items).forEach(item => {
                const { serverName } = item, setting = __rest(item, ["serverName"]);
                settings[serverName] = setting;
            });
            this._setting.set(SETTING_NAME, settings).catch(console.error);
        };
        this._setting = props.formContext.settings;
        this._trans = props.translator.load('jupyterlab');
        const schema = this._setting.schema['definitions'];
        this._defaultSetting = schema['languageServer']['default'];
        this._schema = schema['languageServer']['properties'];
        const title = props.schema.title;
        const desc = props.schema.description;
        const settings = props.formContext.settings;
        const compositeData = settings.get(SETTING_NAME).composite;
        let items = {};
        if (compositeData) {
            Object.entries(compositeData).forEach(([key, value]) => {
                if (value) {
                    const hash = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.UUID.uuid4();
                    items[hash] = Object.assign({ serverName: key }, value);
                }
            });
        }
        this.state = { title, desc, items };
        this._debouncedUpdateSetting = new _lumino_polling__WEBPACK_IMPORTED_MODULE_2__.Debouncer(this.updateSetting.bind(this));
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", null,
            react__WEBPACK_IMPORTED_MODULE_3___default().createElement("fieldset", null,
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("legend", null, this.state.title),
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("p", { className: "field-description" }, this.state.desc),
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", { className: "field field-array field-array-of-object" }, Object.entries(this.state.items).map(([hash, value], idx) => {
                    return (react__WEBPACK_IMPORTED_MODULE_3___default().createElement(BuildSettingForm, { key: `${idx}-${hash}`, trans: this._trans, removeSetting: this.removeSetting, updateSetting: this._debouncedUpdateSetting, serverHash: hash, settings: value, schema: this._schema }));
                })),
                react__WEBPACK_IMPORTED_MODULE_3___default().createElement("div", null,
                    react__WEBPACK_IMPORTED_MODULE_3___default().createElement("button", { style: { margin: 2 }, className: "jp-mod-styled jp-mod-reject", onClick: this.addServerSetting }, this._trans.__('Add server'))))));
    }
}
/**
 * Custom setting renderer for language server extension.
 */
function renderServerSetting(props, translator) {
    return react__WEBPACK_IMPORTED_MODULE_3___default().createElement(SettingRenderer, Object.assign({}, props, { translator: translator }));
}


/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfbHNwLWV4dGVuc2lvbl9saWJfaW5kZXhfanMuNjMwOGFjOWY0ZmVlNDc1MjllMTQuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUEsMENBQTBDO0FBQzFDLDJEQUEyRDtBQUMzRDs7O0dBR0c7QUFtQnNCO0FBQ3VEO0FBQ2pCO0FBQ1Q7QUFLbkI7QUFFUTtBQUVNO0FBR2pELE1BQU0sTUFBTSxHQUF5RDtJQUNuRSxRQUFRO0lBQ1IsRUFBRSxFQUFFLGtDQUFrQztJQUN0QyxRQUFRLEVBQUUsQ0FBQyx5RUFBZ0IsRUFBRSxnRUFBVyxDQUFDO0lBQ3pDLFFBQVEsRUFBRSxDQUFDLHdFQUF1QixFQUFFLDZFQUFzQixDQUFDO0lBQzNELFFBQVEsRUFBRSwwRUFBNkI7SUFDdkMsU0FBUyxFQUFFLElBQUk7Q0FDaEIsQ0FBQztBQUVGLE1BQU0sYUFBYSxHQUE4QztJQUMvRCxFQUFFLEVBQUUsbUNBQW1DO0lBQ3ZDLFFBQVEsRUFBRSxHQUFHLEVBQUUsQ0FBQyxJQUFJLDJEQUFjLEVBQUU7SUFDcEMsUUFBUSxFQUFFLCtEQUFrQjtJQUM1QixTQUFTLEVBQUUsSUFBSTtDQUNoQixDQUFDO0FBRUYsTUFBTSwwQkFBMEIsR0FDOUI7SUFDRSxFQUFFLEVBQUUsMkVBQThCO0lBQ2xDLFFBQVEsRUFBRSxHQUFHLENBQUMsRUFBRTtRQUNkLE1BQU0sZ0JBQWdCLEdBQUcsSUFBSSxrRUFBcUIsRUFBRSxDQUFDO1FBRXJELE1BQU0scUJBQXFCLEdBQUcsSUFBSSxxRUFBd0IsQ0FBQztZQUN6RCxRQUFRLEVBQUUsVUFBVTtZQUNwQixZQUFZLEVBQUUsS0FBSztZQUNuQixjQUFjLEVBQUUsSUFBSTtZQUNwQixRQUFRLEVBQUUsQ0FBQyxVQUFVLENBQUM7U0FDdkIsQ0FBQyxDQUFDO1FBQ0gsZ0JBQWdCLENBQUMsUUFBUSxDQUFDLHFCQUFxQixFQUFFLElBQUksQ0FBQyxDQUFDO1FBQ3ZELE1BQU0sZ0JBQWdCLEdBQUcsSUFBSSxxRUFB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QUM7SUFDSixDQUFDO0NBMkJGO0FBRUQ7O0dBRUc7QUFDSSxTQUFTLG1CQUFtQixDQUNqQyxLQUFpQixFQUNqQixVQUF1QjtJQUV2QixPQUFPLDJEQUFDLGVBQWUsb0JBQUssS0FBSyxJQUFFLFVBQVUsRUFBRSxVQUFVLElBQUksQ0FBQztBQUNoRSxDQUFDIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vQGp1cHl0ZXJsYWIvYXBwbGljYXRpb24tdG9wLy4uLy4uL3BhY2thZ2VzL2xzcC1leHRlbnNpb24vc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9sc3AtZXh0ZW5zaW9uL3NyYy9yZW5kZXJlci50c3giXSwic291cmNlc0NvbnRlbnQiOlsiLy8gQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG4vLyBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxuLyoqXG4gKiBAcGFja2FnZURvY3VtZW50YXRpb25cbiAqIEBtb2R1bGUgbHNwLWV4dGVuc2lvblxuICovXG5cbmltcG9ydCB7XG4gIEp1cHl0ZXJGcm9udEVuZCxcbiAgSnVweXRlckZyb250RW5kUGx1Z2luXG59IGZyb20gJ0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uJztcbmltcG9ydCB7XG4gIENvZGVFeHRyYWN0b3JzTWFuYWdlcixcbiAgRG9jdW1lbnRDb25uZWN0aW9uTWFuYWdlcixcbiAgRmVhdHVyZU1hbmFnZXIsXG4gIElMU1BDb2RlRXh0cmFjdG9yc01hbmFnZXIsXG4gIElMU1BDb25uZWN0aW9uLFxuICBJTFNQRG9jdW1lbnRDb25uZWN0aW9uTWFuYWdlcixcbiAgSUxTUEZlYXR1cmVNYW5hZ2VyLFxuICBMYW5ndWFnZVNlcnZlck1hbmFnZXIsXG4gIExhbmd1YWdlU2VydmVycyxcbiAgVGV4dEZvcmVpZ25Db2RlRXh0cmFjdG9yLFxuICBUTGFuZ3VhZ2VTZXJ2ZXJDb25maWd1cmF0aW9ucyxcbiAgVExhbmd1YWdlU2VydmVySWRcbn0gZnJvbSAnQGp1cHl0ZXJsYWIvbHNwJztcbmltcG9ydCB7IElSdW5uaW5nU2Vzc2lvbk1hbmFnZXJzLCBJUnVubmluZ1Nlc3Npb25zIH0gZnJvbSAnQGp1cHl0ZXJsYWIvcnVubmluZyc7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnQGp1cHl0ZXJsYWIvc2V0dGluZ3JlZ2lzdHJ5JztcbmltcG9ydCB7IElUcmFuc2xhdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHtcbiAgSUZvcm1Db21wb25lbnRSZWdpc3RyeSxcbiAgTGFiSWNvbixcbiAgcHl0aG9uSWNvblxufSBmcm9tICdAanVweXRlcmxhYi91aS1jb21wb25lbnRzJztcbmltcG9ydCB7IFBhcnRpYWxKU09OT2JqZWN0IH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuXG5pbXBvcnQgeyByZW5kZXJTZXJ2ZXJTZXR0aW5nIH0gZnJvbSAnLi9yZW5kZXJlcic7XG5cbmltcG9ydCB0eXBlIHsgRmllbGRQcm9wcyB9IGZyb20gJ0ByanNmL2NvcmUnO1xuY29uc3QgcGx1Z2luOiBKdXB5dGVyRnJvbnRFbmRQbHVnaW48SUxTUERvY3VtZW50Q29ubmVjdGlvbk1hbmFnZXI+ID0ge1xuICBhY3RpdmF0ZSxcbiAgaWQ6ICdAanVweXRlcmxhYi9sc3AtZXh0ZW5zaW9uOnBsdWdpbicsXG4gIHJlcXVpcmVzOiBbSVNldHRpbmdSZWdpc3RyeSwgSVRyYW5zbGF0b3JdLFxuICBvcHRpb25hbDogW0lSdW5uaW5nU2Vzc2lvbk1hbmFnZXJzLCBJRm9ybUNvbXBvbmVudFJlZ2lzdHJ5XSxcbiAgcHJvdmlkZXM6IElMU1BEb2N1bWVudENvbm5lY3Rpb25NYW5hZ2VyLFxuICBhdXRvU3RhcnQ6IHRydWVcbn07XG5cbmNvbnN0IGZlYXR1cmVQbHVnaW46IEp1cHl0ZXJGcm9udEVuZFBsdWdpbjxJTFNQRmVhdHVyZU1hbmFnZXI+ID0ge1xuICBpZDogJ0BqdXB5dGVybGFiL2xzcC1leHRlbnNpb246ZmVhdHVyZScsXG4gIGFjdGl2YXRlOiAoKSA9PiBuZXcgRmVhdHVyZU1hbmFnZXIoKSxcbiAgcHJvdmlkZXM6IElMU1BGZWF0dXJlTWFuYWdlcixcbiAgYXV0b1N0YXJ0OiB0cnVlXG59O1xuXG5jb25zdCBjb2RlRXh0cmFjdG9yTWFuYWdlclBsdWdpbjogSnVweXRlckZyb250RW5kUGx1Z2luPElMU1BDb2RlRXh0cmFjdG9yc01hbmFnZXI+ID1cbiAge1xuICAgIGlkOiBJTFNQQ29kZUV4dHJhY3RvcnNNYW5hZ2VyLm5hbWUsXG4gICAgYWN0aXZhdGU6IGFwcCA9PiB7XG4gICAgICBjb25zdCBleHRyYWN0b3JNYW5hZ2VyID0gbmV3IENvZGVFeHRyYWN0b3JzTWFuYWdlcigpO1xuXG4gICAgICBjb25zdCBtYXJrZG93bkNlbGxFeHRyYWN0b3IgPSBuZXcgVGV4dEZvcmVpZ25Db2RlRXh0cmFjdG9yKHtcbiAgICAgICAgbGFuZ3VhZ2U6ICdtYXJrZG93bicsXG4gICAgICAgIGlzU3RhbmRhbG9uZTogZmFsc2UsXG4gICAgICAgIGZpbGVfZXh0ZW5zaW9uOiAnbWQnLFxuICAgICAgICBjZWxsVHlwZTogWydtYXJrZG93biddXG4gICAgICB9KTtcbiAgICAgIGV4dHJhY3Rvck1hbmFnZXIucmVnaXN0ZXIobWFya2Rvd25DZWxsRXh0cmFjdG9yLCBudWxsKTtcbiAgICAgIGNvbnN0IHJhd0NlbGxFeHRyYWN0b3IgPSBuZXcgVGV4dEZvcmVpZ25Db2RlRXh0cmFjdG9yKHtcbiAgICAgICAgbGFuZ3VhZ2U6ICd0ZXh0JyxcbiAgICAgICAgaXNTdGFuZGFsb25lOiBmYWxzZSxcbiAgICAgICAgZmlsZV9leHRlbnNpb246ICd0eHQnLFxuICAgICAgICBjZWxsVHlwZTogWydyYXcnXVxuICAgICAgfSk7XG4gICAgICBleHRyYWN0b3JNYW5hZ2VyLnJlZ2lzdGVyKHJhd0NlbGxFeHRyYWN0b3IsIG51bGwpO1xuICAgICAgcmV0dXJuIGV4dHJhY3Rvck1hbmFnZXI7XG4gICAgfSxcbiAgICBwcm92aWRlczogSUxTUENvZGVFeHRyYWN0b3JzTWFuYWdlcixcbiAgICBhdXRvU3RhcnQ6IHRydWVcbiAgfTtcblxuLyoqXG4gKiBBY3RpdmF0ZSB0aGUgbHNwIHBsdWdpbi5cbiAqL1xuZnVuY3Rpb24gYWN0aXZhdGUoXG4gIGFwcDogSnVweXRlckZyb250RW5kLFxuICBzZXR0aW5nUmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnksXG4gIHRyYW5zbGF0b3I6IElUcmFuc2xhdG9yLFxuICBydW5uaW5nU2Vzc2lvbk1hbmFnZXJzOiBJUnVubmluZ1Nlc3Npb25NYW5hZ2VycyB8IG51bGwsXG4gIHNldHRpbmdSZW5kZXJlclJlZ2lzdHJ5OiBJRm9ybUNvbXBvbmVudFJlZ2lzdHJ5IHwgbnVsbFxuKTogSUxTUERvY3VtZW50Q29ubmVjdGlvbk1hbmFnZXIge1xuICBjb25zdCBMQU5HVUFHRV9TRVJWRVJTID0gJ2xhbmd1YWdlU2VydmVycyc7XG4gIGNvbnN0IGxhbmd1YWdlU2VydmVyTWFuYWdlciA9IG5ldyBMYW5ndWFnZVNlcnZlck1hbmFnZXIoe30pO1xuICBjb25zdCBjb25uZWN0aW9uTWFuYWdlciA9IG5ldyBEb2N1bWVudENvbm5lY3Rpb25NYW5hZ2VyKHtcbiAgICBsYW5ndWFnZVNlcnZlck1hbmFnZXJcbiAgfSk7XG5cbiAgY29uc3QgdXBkYXRlT3B0aW9ucyA9IChzZXR0aW5nczogSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3MpID0+IHtcbiAgICBjb25zdCBvcHRpb25zID0gc2V0dGluZ3MuY29tcG9zaXRlIGFzIFJlcXVpcmVkPExhbmd1YWdlU2VydmVycz47XG4gICAgY29uc3QgbGFuZ3VhZ2VTZXJ2ZXJTZXR0aW5ncyA9IChvcHRpb25zLmxhbmd1YWdlU2VydmVycyB8fFxuICAgICAge30pIGFzIFRMYW5ndWFnZVNlcnZlckNvbmZpZ3VyYXRpb25zO1xuXG4gICAgY29ubmVjdGlvbk1hbmFnZXIuaW5pdGlhbENvbmZpZ3VyYXRpb25zID0gbGFuZ3VhZ2VTZXJ2ZXJTZXR0aW5ncztcbiAgICAvLyBUT0RPOiBpZiBwcmlvcml0aWVzIGNoYW5nZWQgcmVzZXQgY29ubmVjdGlvbnNcbiAgICBjb25uZWN0aW9uTWFuYWdlci51cGRhdGVDb25maWd1cmF0aW9uKGxhbmd1YWdlU2VydmVyU2V0dGluZ3MpO1xuICAgIGNvbm5lY3Rpb25NYW5hZ2VyLnVwZGF0ZVNlcnZlckNvbmZpZ3VyYXRpb25zKGxhbmd1YWdlU2VydmVyU2V0dGluZ3MpO1xuICAgIGNvbm5lY3Rpb25NYW5hZ2VyLnVwZGF0ZUxvZ2dpbmcoXG4gICAgICBvcHRpb25zLmxvZ0FsbENvbW11bmljYXRpb24sXG4gICAgICBvcHRpb25zLnNldFRyYWNlXG4gICAgKTtcbiAgfTtcblxuICBzZXR0aW5nUmVnaXN0cnkudHJhbnNmb3JtKHBsdWdpbi5pZCwge1xuICAgIGZldGNoOiBwbHVnaW4gPT4ge1xuICAgICAgY29uc3Qgc2NoZW1hID0gcGx1Z2luLnNjaGVtYS5wcm9wZXJ0aWVzITtcbiAgICAgIGNvbnN0IGRlZmF1bHRWYWx1ZTogeyBba2V5OiBzdHJpbmddOiBhbnkgfSA9IHt9O1xuICAgICAgbGFuZ3VhZ2VTZXJ2ZXJNYW5hZ2VyLnNlc3Npb25zLmZvckVhY2goKF8sIGtleSkgPT4ge1xuICAgICAgICBkZWZhdWx0VmFsdWVba2V5XSA9IHsgcmFuazogNTAsIGNvbmZpZ3VyYXRpb246IHt9IH07XG4gICAgICB9KTtcblxuICAgICAgc2NoZW1hW0xBTkdVQUdFX1NFUlZFUlNdWydkZWZhdWx0J10gPSBkZWZhdWx0VmFsdWU7XG4gICAgICByZXR1cm4gcGx1Z2luO1xuICAgIH0sXG4gICAgY29tcG9zZTogcGx1Z2luID0+IHtcbiAgICAgIGNvbnN0IHByb3BlcnRpZXMgPSBwbHVnaW4uc2NoZW1hLnByb3BlcnRpZXMhO1xuICAgICAgY29uc3QgdXNlciA9IHBsdWdpbi5kYXRhLnVzZXI7XG5cbiAgICAgIGNvbnN0IHNlcnZlckRlZmF1bHRTZXR0aW5ncyA9IHByb3BlcnRpZXNbTEFOR1VBR0VfU0VSVkVSU11bXG4gICAgICAgICdkZWZhdWx0J1xuICAgICAgXSBhcyBQYXJ0aWFsSlNPTk9iamVjdDtcbiAgICAgIGNvbnN0IHNlcnZlclVzZXJTZXR0aW5ncyA9IHVzZXJbTEFOR1VBR0VfU0VSVkVSU10gYXNcbiAgICAgICAgfCBQYXJ0aWFsSlNPTk9iamVjdFxuICAgICAgICB8IHVuZGVmaW5lZDtcbiAgICAgIGxldCBzZXJ2ZXJDb21wb3NpdGUgPSB7IC4uLnNlcnZlckRlZmF1bHRTZXR0aW5ncyB9O1xuICAgICAgaWYgKHNlcnZlclVzZXJTZXR0aW5ncykge1xuICAgICAgICBzZXJ2ZXJDb21wb3NpdGUgPSB7IC4uLnNlcnZlckNvbXBvc2l0ZSwgLi4uc2VydmVyVXNlclNldHRpbmdzIH07XG4gICAgICB9XG4gICAgICBjb25zdCBjb21wb3NpdGU6IHsgW2tleTogc3RyaW5nXTogYW55IH0gPSB7XG4gICAgICAgIFtMQU5HVUFHRV9TRVJWRVJTXTogc2VydmVyQ29tcG9zaXRlXG4gICAgICB9O1xuICAgICAgT2JqZWN0LmVudHJpZXMocHJvcGVydGllcykuZm9yRWFjaCgoW2tleSwgdmFsdWVdKSA9PiB7XG4gICAgICAgIGlmIChrZXkgIT09IExBTkdVQUdFX1NFUlZFUlMpIHtcbiAgICAgICAgICBpZiAoa2V5IGluIHVzZXIpIHtcbiAgICAgICAgICAgIGNvbXBvc2l0ZVtrZXldID0gdXNlcltrZXldO1xuICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICBjb21wb3NpdGVba2V5XSA9IHZhbHVlLmRlZmF1bHQ7XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICB9KTtcbiAgICAgIHBsdWdpbi5kYXRhLmNvbXBvc2l0ZSA9IGNvbXBvc2l0ZTtcbiAgICAgIHJldHVybiBwbHVnaW47XG4gICAgfVxuICB9KTtcbiAgbGFuZ3VhZ2VTZXJ2ZXJNYW5hZ2VyLnNlc3Npb25zQ2hhbmdlZC5jb25uZWN0KGFzeW5jICgpID0+IHtcbiAgICBhd2FpdCBzZXR0aW5nUmVnaXN0cnkucmVsb2FkKHBsdWdpbi5pZCk7XG4gIH0pO1xuXG4gIHNldHRpbmdSZWdpc3RyeVxuICAgIC5sb2FkKHBsdWdpbi5pZClcbiAgICAudGhlbihzZXR0aW5ncyA9PiB7XG4gICAgICB1cGRhdGVPcHRpb25zKHNldHRpbmdzKTtcbiAgICAgIHNldHRpbmdzLmNoYW5nZWQuY29ubmVjdCgoKSA9PiB7XG4gICAgICAgIHVwZGF0ZU9wdGlvbnMoc2V0dGluZ3MpO1xuICAgICAgfSk7XG4gICAgfSlcbiAgICAuY2F0Y2goKHJlYXNvbjogRXJyb3IpID0+IHtcbiAgICAgIGNvbnNvbGUuZXJyb3IocmVhc29uLm1lc3NhZ2UpO1xuICAgIH0pO1xuICAvLyBBZGQgYSBzZXNzaW9ucyBtYW5hZ2VyIGlmIHRoZSBydW5uaW5nIGV4dGVuc2lvbiBpcyBhdmFpbGFibGVcbiAgaWYgKHJ1bm5pbmdTZXNzaW9uTWFuYWdlcnMpIHtcbiAgICBhZGRSdW5uaW5nU2Vzc2lvbk1hbmFnZXIoXG4gICAgICBydW5uaW5nU2Vzc2lvbk1hbmFnZXJzLFxuICAgICAgY29ubmVjdGlvbk1hbmFnZXIsXG4gICAgICB0cmFuc2xhdG9yXG4gICAgKTtcbiAgfVxuXG4gIGlmIChzZXR0aW5nUmVuZGVyZXJSZWdpc3RyeSkge1xuICAgIHNldHRpbmdSZW5kZXJlclJlZ2lzdHJ5LmFkZFJlbmRlcmVyKFxuICAgICAgTEFOR1VBR0VfU0VSVkVSUyxcbiAgICAgIChwcm9wczogRmllbGRQcm9wcykgPT4ge1xuICAgICAgICByZXR1cm4gcmVuZGVyU2VydmVyU2V0dGluZyhwcm9wcywgdHJhbnNsYXRvcik7XG4gICAgICB9XG4gICAgKTtcbiAgfVxuXG4gIHJldHVybiBjb25uZWN0aW9uTWFuYWdlcjtcbn1cblxuZXhwb3J0IGNsYXNzIFJ1bm5pbmdMYW5ndWFnZVNlcnZlcnMgaW1wbGVtZW50cyBJUnVubmluZ1Nlc3Npb25zLklSdW5uaW5nSXRlbSB7XG4gIGNvbnN0cnVjdG9yKFxuICAgIGNvbm5lY3Rpb246IElMU1BDb25uZWN0aW9uLFxuICAgIG1hbmFnZXI6IElMU1BEb2N1bWVudENvbm5lY3Rpb25NYW5hZ2VyXG4gICkge1xuICAgIHRoaXMuX2Nvbm5lY3Rpb24gPSBjb25uZWN0aW9uO1xuICAgIHRoaXMuX21hbmFnZXIgPSBtYW5hZ2VyO1xuICB9XG4gIC8qKlxuICAgKiBUaGlzIGlzIG5vLW9wIGJlY2F1c2Ugd2UgZG8gbm90IGRvIGFueXRoaW5nIG9uIHNlcnZlciBjbGljayBldmVudFxuICAgKi9cbiAgb3BlbigpOiB2b2lkIHtcbiAgICAvKiogbm8tb3AgKi9cbiAgfVxuICBpY29uKCk6IExhYkljb24ge1xuICAgIHJldHVybiBweXRob25JY29uO1xuICB9XG4gIGxhYmVsKCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIGAke3RoaXMuX2Nvbm5lY3Rpb24uc2VydmVySWRlbnRpZmllciA/PyAnJ30gKCR7XG4gICAgICB0aGlzLl9jb25uZWN0aW9uLnNlcnZlckxhbmd1YWdlID8/ICcnXG4gICAgfSlgO1xuICB9XG4gIHNodXRkb3duKCk6IHZvaWQge1xuICAgIGZvciAoY29uc3QgW2tleSwgdmFsdWVdIG9mIHRoaXMuX21hbmFnZXIuY29ubmVjdGlvbnMuZW50cmllcygpKSB7XG4gICAgICBpZiAodmFsdWUgPT09IHRoaXMuX2Nvbm5lY3Rpb24pIHtcbiAgICAgICAgY29uc3QgZG9jdW1lbnQgPSB0aGlzLl9tYW5hZ2VyLmRvY3VtZW50cy5nZXQoa2V5KSE7XG4gICAgICAgIHRoaXMuX21hbmFnZXIudW5yZWdpc3RlckRvY3VtZW50KGRvY3VtZW50KTtcbiAgICAgIH1cbiAgICB9XG4gICAgdGhpcy5fbWFuYWdlci5kaXNjb25uZWN0KFxuICAgICAgdGhpcy5fY29ubmVjdGlvbi5zZXJ2ZXJJZGVudGlmaWVyIGFzIFRMYW5ndWFnZVNlcnZlcklkXG4gICAgKTtcbiAgfVxuICBwcml2YXRlIF9jb25uZWN0aW9uOiBJTFNQQ29ubmVjdGlvbjtcbiAgcHJpdmF0ZSBfbWFuYWdlcjogSUxTUERvY3VtZW50Q29ubmVjdGlvbk1hbmFnZXI7XG59XG5cbi8qKlxuICogQWRkIHRoZSBydW5uaW5nIHRlcm1pbmFsIG1hbmFnZXIgdG8gdGhlIHJ1bm5pbmcgcGFuZWwuXG4gKi9cbmZ1bmN0aW9uIGFkZFJ1bm5pbmdTZXNzaW9uTWFuYWdlcihcbiAgbWFuYWdlcnM6IElSdW5uaW5nU2Vzc2lvbk1hbmFnZXJzLFxuICBsc01hbmFnZXI6IElMU1BEb2N1bWVudENvbm5lY3Rpb25NYW5hZ2VyLFxuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvclxuKSB7XG4gIGNvbnN0IHRyYW5zID0gdHJhbnNsYXRvci5sb2FkKCdqdXB5dGVybGFiJyk7XG4gIGNvbnN0IHNpZ25hbCA9IG5ldyBTaWduYWw8YW55LCBhbnk+KGxzTWFuYWdlcik7XG4gIGxzTWFuYWdlci5jb25uZWN0ZWQuY29ubmVjdCgoKSA9PiBzaWduYWwuZW1pdChsc01hbmFnZXIpKTtcbiAgbHNNYW5hZ2VyLmRpc2Nvbm5lY3RlZC5jb25uZWN0KCgpID0+IHNpZ25hbC5lbWl0KGxzTWFuYWdlcikpO1xuICBsc01hbmFnZXIuY2xvc2VkLmNvbm5lY3QoKCkgPT4gc2lnbmFsLmVtaXQobHNNYW5hZ2VyKSk7XG4gIGxzTWFuYWdlci5kb2N1bWVudHNDaGFuZ2VkLmNvbm5lY3QoKCkgPT4gc2lnbmFsLmVtaXQobHNNYW5hZ2VyKSk7XG4gIGxldCBjdXJyZW50UnVubmluZzogUnVubmluZ0xhbmd1YWdlU2VydmVyc1tdID0gW107XG4gIG1hbmFnZXJzLmFkZCh7XG4gICAgbmFtZTogdHJhbnMuX18oJ0xhbmd1YWdlIHNlcnZlcnMnKSxcbiAgICBydW5uaW5nOiAoKSA9PiB7XG4gICAgICBjb25zdCBjb25uZWN0aW9ucyA9IG5ldyBTZXQoWy4uLmxzTWFuYWdlci5jb25uZWN0aW9ucy52YWx1ZXMoKV0pO1xuICAgICAgY3VycmVudFJ1bm5pbmcgPSBbLi4uY29ubmVjdGlvbnNdLm1hcChcbiAgICAgICAgY29ubiA9PiBuZXcgUnVubmluZ0xhbmd1YWdlU2VydmVycyhjb25uLCBsc01hbmFnZXIpXG4gICAgICApO1xuICAgICAgcmV0dXJuIGN1cnJlbnRSdW5uaW5nO1xuICAgIH0sXG4gICAgc2h1dGRvd25BbGw6ICgpID0+IHtcbiAgICAgIGN1cnJlbnRSdW5uaW5nLmZvckVhY2goaXRlbSA9PiB7XG4gICAgICAgIGl0ZW0uc2h1dGRvd24oKTtcbiAgICAgIH0pO1xuICAgIH0sXG4gICAgcmVmcmVzaFJ1bm5pbmc6ICgpID0+IHtcbiAgICAgIHJldHVybiB2b2lkIDA7XG4gICAgfSxcbiAgICBydW5uaW5nQ2hhbmdlZDogc2lnbmFsLFxuICAgIHNodXRkb3duTGFiZWw6IHRyYW5zLl9fKCdTaHV0IERvd24nKSxcbiAgICBzaHV0ZG93bkFsbExhYmVsOiB0cmFucy5fXygnU2h1dCBEb3duIEFsbCcpLFxuICAgIHNodXRkb3duQWxsQ29uZmlybWF0aW9uVGV4dDogdHJhbnMuX18oXG4gICAgICAnQXJlIHlvdSBzdXJlIHlvdSB3YW50IHRvIHBlcm1hbmVudGx5IHNodXQgZG93biBhbGwgcnVubmluZyBsYW5ndWFnZSBzZXJ2ZXJzPydcbiAgICApXG4gIH0pO1xufVxuLyoqXG4gKiBFeHBvcnQgdGhlIHBsdWdpbiBhcyBkZWZhdWx0LlxuICovXG5leHBvcnQgZGVmYXVsdCBbcGx1Z2luLCBmZWF0dXJlUGx1Z2luLCBjb2RlRXh0cmFjdG9yTWFuYWdlclBsdWdpbl07XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElTZXR0aW5nUmVnaXN0cnkgfSBmcm9tICdAanVweXRlcmxhYi9zZXR0aW5ncmVnaXN0cnknO1xuaW1wb3J0IHsgSVRyYW5zbGF0b3IsIFRyYW5zbGF0aW9uQnVuZGxlIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdHJhbnNsYXRpb24nO1xuaW1wb3J0IHsgY2xvc2VJY29uIH0gZnJvbSAnQGp1cHl0ZXJsYWIvdWktY29tcG9uZW50cyc7XG5pbXBvcnQgeyBVVUlEIH0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgRGVib3VuY2VyIH0gZnJvbSAnQGx1bWluby9wb2xsaW5nJztcbmltcG9ydCBSZWFjdCwgeyB1c2VTdGF0ZSB9IGZyb20gJ3JlYWN0JztcblxuaW1wb3J0IHR5cGUgeyBGaWVsZFByb3BzIH0gZnJvbSAnQHJqc2YvY29yZSc7XG50eXBlIFREaWN0ID0geyBba2V5OiBzdHJpbmddOiBhbnkgfTtcblxuaW50ZXJmYWNlIElTZXR0aW5nUHJvcGVydHlNYXAge1xuICBba2V5OiBzdHJpbmddOiBJU2V0dGluZ1Byb3BlcnR5O1xufVxuaW50ZXJmYWNlIElTZXR0aW5nUHJvcGVydHkge1xuICAvKipcbiAgICogTmFtZSBvZiBzZXR0aW5nIHByb3BlcnR5XG4gICAqL1xuICBwcm9wZXJ0eTogc3RyaW5nO1xuICAvKipcbiAgICogVHlwZSBvZiBzZXR0aW5nIHByb3BlcnR5XG4gICAqL1xuICB0eXBlOiAnYm9vbGVhbicgfCAnc3RyaW5nJyB8ICdudW1iZXInO1xuICAvKipcbiAgICogVmFsdWUgb2Ygc2V0dGluZyBwcm9wZXJ0eVxuICAgKi9cbiAgdmFsdWU6IGFueTtcbn1cbmNvbnN0IFNFVFRJTkdfTkFNRSA9ICdsYW5ndWFnZVNlcnZlcnMnO1xuY29uc3QgU0VSVkVSX1NFVFRJTkdTID0gJ2NvbmZpZ3VyYXRpb24nO1xuXG5pbnRlcmZhY2UgSVNldHRpbmdGb3JtUHJvcHMge1xuICAvKipcbiAgICogVGhlIHRyYW5zbGF0aW9uIGJ1bmRsZS5cbiAgICovXG4gIHRyYW5zOiBUcmFuc2xhdGlvbkJ1bmRsZTtcblxuICAvKipcbiAgICogQ2FsbGJhY2sgdG8gcmVtb3ZlIHNldHRpbmcgaXRlbS5cbiAgICovXG4gIHJlbW92ZVNldHRpbmc6IChrZXk6IHN0cmluZykgPT4gdm9pZDtcblxuICAvKipcbiAgICogQ2FsbGJhY2sgdG8gdXBkYXRlIHRoZSBzZXR0aW5nIGl0ZW0uXG4gICAqL1xuICB1cGRhdGVTZXR0aW5nOiBEZWJvdW5jZXI8dm9pZCwgYW55LCBbaGFzaDogc3RyaW5nLCBuZXdTZXR0aW5nOiBURGljdF0+O1xuXG4gIC8qKlxuICAgKiBIYXNoIHRvIGRpZmZlcmVudGlhdGUgdGhlIHNldHRpbmcgZmllbGRzLlxuICAgKi9cbiAgc2VydmVySGFzaDogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiAgU2V0dGluZyB2YWx1ZS5cbiAgICovXG4gIHNldHRpbmdzOiBURGljdDtcblxuICAvKipcbiAgICogU2V0dGluZyBzY2hlbWEuXG4gICAqL1xuICBzY2hlbWE6IFREaWN0O1xufVxuXG4vKipcbiAqIFRoZSBSZWFjdCBjb21wb25lbnQgb2YgdGhlIHNldHRpbmcgZmllbGRcbiAqL1xuZnVuY3Rpb24gQnVpbGRTZXR0aW5nRm9ybShwcm9wczogSVNldHRpbmdGb3JtUHJvcHMpOiBKU1guRWxlbWVudCB7XG4gIGNvbnN0IHsgW1NFUlZFUl9TRVRUSU5HU106IHNlcnZlclNldHRpbmdzU2NoZW1hLCAuLi5vdGhlclNldHRpbmdzU2NoZW1hIH0gPVxuICAgIHByb3BzLnNjaGVtYTtcbiAgY29uc3Qge1xuICAgIFtTRVJWRVJfU0VUVElOR1NdOiBzZXJ2ZXJTZXR0aW5ncyxcbiAgICBzZXJ2ZXJOYW1lLFxuICAgIC4uLm90aGVyU2V0dGluZ3NcbiAgfSA9IHByb3BzLnNldHRpbmdzO1xuXG4gIGNvbnN0IFtjdXJyZW50U2VydmVyTmFtZSwgc2V0Q3VycmVudFNlcnZlck5hbWVdID1cbiAgICB1c2VTdGF0ZTxzdHJpbmc+KHNlcnZlck5hbWUpO1xuXG4gIC8qKlxuICAgKiBDYWxsYmFjayBvbiBzZXJ2ZXIgbmFtZSBmaWVsZCBjaGFuZ2UgZXZlbnRcbiAgICovXG4gIGNvbnN0IG9uU2VydmVyTmFtZUNoYW5nZSA9IChlOiBSZWFjdC5DaGFuZ2VFdmVudDxIVE1MSW5wdXRFbGVtZW50PikgPT4ge1xuICAgIHByb3BzLnVwZGF0ZVNldHRpbmdcbiAgICAgIC5pbnZva2UocHJvcHMuc2VydmVySGFzaCwge1xuICAgICAgICBzZXJ2ZXJOYW1lOiBlLnRhcmdldC52YWx1ZVxuICAgICAgfSlcbiAgICAgIC5jYXRjaChjb25zb2xlLmVycm9yKTtcbiAgICBzZXRDdXJyZW50U2VydmVyTmFtZShlLnRhcmdldC52YWx1ZSk7XG4gIH07XG5cbiAgY29uc3Qgc2VydmVyU2V0dGluZ1dpdGhUeXBlOiBJU2V0dGluZ1Byb3BlcnR5TWFwID0ge307XG4gIE9iamVjdC5lbnRyaWVzKHNlcnZlclNldHRpbmdzKS5mb3JFYWNoKChba2V5LCB2YWx1ZV0pID0+IHtcbiAgICBjb25zdCBuZXdQcm9wczogSVNldHRpbmdQcm9wZXJ0eSA9IHtcbiAgICAgIHByb3BlcnR5OiBrZXksXG4gICAgICB0eXBlOiB0eXBlb2YgdmFsdWUgYXMgJ3N0cmluZycgfCAnbnVtYmVyJyB8ICdib29sZWFuJyxcbiAgICAgIHZhbHVlXG4gICAgfTtcbiAgICBzZXJ2ZXJTZXR0aW5nV2l0aFR5cGVbVVVJRC51dWlkNCgpXSA9IG5ld1Byb3BzO1xuICB9KTtcblxuICBjb25zdCBbcHJvcGVydHlNYXAsIHNldFByb3BlcnR5TWFwXSA9IHVzZVN0YXRlPElTZXR0aW5nUHJvcGVydHlNYXA+KFxuICAgIHNlcnZlclNldHRpbmdXaXRoVHlwZVxuICApO1xuXG4gIGNvbnN0IGRlZmF1bHRPdGhlclNldHRpbmdzOiBURGljdCA9IHt9O1xuXG4gIE9iamVjdC5lbnRyaWVzKG90aGVyU2V0dGluZ3NTY2hlbWEpLmZvckVhY2goKFtrZXksIHZhbHVlXSkgPT4ge1xuICAgIGlmIChrZXkgaW4gb3RoZXJTZXR0aW5ncykge1xuICAgICAgZGVmYXVsdE90aGVyU2V0dGluZ3Nba2V5XSA9IG90aGVyU2V0dGluZ3Nba2V5XTtcbiAgICB9IGVsc2Uge1xuICAgICAgZGVmYXVsdE90aGVyU2V0dGluZ3Nba2V5XSA9IHZhbHVlWydkZWZhdWx0J107XG4gICAgfVxuICB9KTtcblxuICBjb25zdCBbb3RoZXJTZXR0aW5nc0NvbXBvc2l0ZSwgc2V0T3RoZXJTZXR0aW5nc0NvbXBvc2l0ZV0gPVxuICAgIHVzZVN0YXRlPFREaWN0PihkZWZhdWx0T3RoZXJTZXR0aW5ncyk7XG5cbiAgLyoqXG4gICAqIENhbGxiYWNrIG9uIGFkZGl0aW9uYWwgc2V0dGluZyBmaWVsZCBjaGFuZ2UgZXZlbnRcbiAgICovXG4gIGNvbnN0IG9uT3RoZXJTZXR0aW5nc0NoYW5nZSA9IChcbiAgICBwcm9wZXJ0eTogc3RyaW5nLFxuICAgIHZhbHVlOiBhbnksXG4gICAgdHlwZTogc3RyaW5nXG4gICkgPT4ge1xuICAgIGxldCBzZXR0aW5nVmFsdWUgPSB2YWx1ZTtcbiAgICBpZiAodHlwZSA9PT0gJ251bWJlcicpIHtcbiAgICAgIHNldHRpbmdWYWx1ZSA9IHBhcnNlRmxvYXQodmFsdWUpO1xuICAgIH1cbiAgICBjb25zdCBuZXdQcm9wcyA9IHtcbiAgICAgIC4uLm90aGVyU2V0dGluZ3NDb21wb3NpdGUsXG4gICAgICBbcHJvcGVydHldOiBzZXR0aW5nVmFsdWVcbiAgICB9O1xuICAgIHByb3BzLnVwZGF0ZVNldHRpbmcuaW52b2tlKHByb3BzLnNlcnZlckhhc2gsIG5ld1Byb3BzKS5jYXRjaChjb25zb2xlLmVycm9yKTtcbiAgICBzZXRPdGhlclNldHRpbmdzQ29tcG9zaXRlKG5ld1Byb3BzKTtcbiAgfTtcblxuICAvKipcbiAgICogQ2FsbGJhY2sgb24gYEFkZCBwcm9wZXJ0eWAgYnV0dG9uIGNsaWNrIGV2ZW50LlxuICAgKi9cbiAgY29uc3QgYWRkUHJvcGVydHkgPSAoKSA9PiB7XG4gICAgY29uc3QgaGFzaCA9IFVVSUQudXVpZDQoKTtcbiAgICBjb25zdCBuZXdNYXA6IElTZXR0aW5nUHJvcGVydHlNYXAgPSB7XG4gICAgICAuLi5wcm9wZXJ0eU1hcCxcbiAgICAgIFtoYXNoXTogeyBwcm9wZXJ0eTogJycsIHR5cGU6ICdzdHJpbmcnLCB2YWx1ZTogJycgfVxuICAgIH07XG4gICAgY29uc3QgcGF5bG9hZDogVERpY3QgPSB7fTtcbiAgICBPYmplY3QudmFsdWVzKG5ld01hcCkuZm9yRWFjaCh2YWx1ZSA9PiB7XG4gICAgICBwYXlsb2FkW3ZhbHVlLnByb3BlcnR5XSA9IHZhbHVlLnZhbHVlO1xuICAgIH0pO1xuICAgIHByb3BzLnVwZGF0ZVNldHRpbmdcbiAgICAgIC5pbnZva2UocHJvcHMuc2VydmVySGFzaCwge1xuICAgICAgICBbU0VSVkVSX1NFVFRJTkdTXTogcGF5bG9hZFxuICAgICAgfSlcbiAgICAgIC5jYXRjaChjb25zb2xlLmVycm9yKTtcbiAgICBzZXRQcm9wZXJ0eU1hcChuZXdNYXApO1xuICB9O1xuXG4gIC8qKlxuICAgKiBDYWxsYmFjayBvbiBgUmVtb3ZlIHByb3BlcnR5YCBidXR0b24gY2xpY2sgZXZlbnQuXG4gICAqL1xuICBjb25zdCByZW1vdmVQcm9wZXJ0eSA9IChlbnRyeUhhc2g6IHN0cmluZykgPT4ge1xuICAgIGNvbnN0IG5ld01hcDogSVNldHRpbmdQcm9wZXJ0eU1hcCA9IHt9O1xuICAgIE9iamVjdC5lbnRyaWVzKHByb3BlcnR5TWFwKS5mb3JFYWNoKChbaGFzaCwgdmFsdWVdKSA9PiB7XG4gICAgICBpZiAoaGFzaCAhPT0gZW50cnlIYXNoKSB7XG4gICAgICAgIG5ld01hcFtoYXNoXSA9IHZhbHVlO1xuICAgICAgfVxuICAgICAgY29uc3QgcGF5bG9hZDogVERpY3QgPSB7fTtcbiAgICAgIE9iamVjdC52YWx1ZXMobmV3TWFwKS5mb3JFYWNoKHZhbHVlID0+IHtcbiAgICAgICAgcGF5bG9hZFt2YWx1ZS5wcm9wZXJ0eV0gPSB2YWx1ZS52YWx1ZTtcbiAgICAgIH0pO1xuICAgICAgcHJvcHMudXBkYXRlU2V0dGluZ1xuICAgICAgICAuaW52b2tlKHByb3BzLnNlcnZlckhhc2gsIHtcbiAgICAgICAgICBbU0VSVkVSX1NFVFRJTkdTXTogcGF5bG9hZFxuICAgICAgICB9KVxuICAgICAgICAuY2F0Y2goY29uc29sZS5lcnJvcik7XG4gICAgICBzZXRQcm9wZXJ0eU1hcChuZXdNYXApO1xuICAgIH0pO1xuICB9O1xuXG4gIC8qKlxuICAgKiBTYXZlIHNldHRpbmcgdG8gdGhlIHNldHRpbmcgcmVnaXN0cnkgb24gZmllbGQgY2hhbmdlIGV2ZW50LlxuICAgKi9cbiAgY29uc3Qgc2V0UHJvcGVydHkgPSAoaGFzaDogc3RyaW5nLCBwcm9wZXJ0eTogSVNldHRpbmdQcm9wZXJ0eSk6IHZvaWQgPT4ge1xuICAgIGlmIChoYXNoIGluIHByb3BlcnR5TWFwKSB7XG4gICAgICBjb25zdCBuZXdNYXA6IElTZXR0aW5nUHJvcGVydHlNYXAgPSB7IC4uLnByb3BlcnR5TWFwLCBbaGFzaF06IHByb3BlcnR5IH07XG4gICAgICBjb25zdCBwYXlsb2FkOiBURGljdCA9IHt9O1xuICAgICAgT2JqZWN0LnZhbHVlcyhuZXdNYXApLmZvckVhY2godmFsdWUgPT4ge1xuICAgICAgICBwYXlsb2FkW3ZhbHVlLnByb3BlcnR5XSA9IHZhbHVlLnZhbHVlO1xuICAgICAgfSk7XG4gICAgICBzZXRQcm9wZXJ0eU1hcChuZXdNYXApO1xuICAgICAgcHJvcHMudXBkYXRlU2V0dGluZ1xuICAgICAgICAuaW52b2tlKHByb3BzLnNlcnZlckhhc2gsIHtcbiAgICAgICAgICBbU0VSVkVSX1NFVFRJTkdTXTogcGF5bG9hZFxuICAgICAgICB9KVxuICAgICAgICAuY2F0Y2goY29uc29sZS5lcnJvcik7XG4gICAgfVxuICB9O1xuICBjb25zdCBkZWJvdW5jZWRTZXRQcm9wZXJ0eSA9IG5ldyBEZWJvdW5jZXI8XG4gICAgdm9pZCxcbiAgICBhbnksXG4gICAgW2hhc2g6IHN0cmluZywgcHJvcGVydHk6IElTZXR0aW5nUHJvcGVydHldXG4gID4oc2V0UHJvcGVydHkpO1xuICByZXR1cm4gKFxuICAgIDxkaXYgY2xhc3NOYW1lPVwiYXJyYXktaXRlbVwiPlxuICAgICAgPGRpdiBjbGFzc05hbWU9XCJmb3JtLWdyb3VwIFwiPlxuICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUZvcm1Hcm91cC1jb250ZW50XCI+XG4gICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1vYmplY3RGaWVsZFdyYXBwZXJcIj5cbiAgICAgICAgICAgIDxmaWVsZHNldD5cbiAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJmb3JtLWdyb3VwIHNtYWxsLWZpZWxkXCI+XG4gICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1tb2RpZmllZEluZGljYXRvciBqcC1lcnJvckluZGljYXRvclwiPjwvZGl2PlxuICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwianAtRm9ybUdyb3VwLWNvbnRlbnRcIj5cbiAgICAgICAgICAgICAgICAgIDxoMyBjbGFzc05hbWU9XCJqcC1Gb3JtR3JvdXAtZmllbGRMYWJlbCBqcC1Gb3JtR3JvdXAtY29udGVudEl0ZW1cIj5cbiAgICAgICAgICAgICAgICAgICAge3Byb3BzLnRyYW5zLl9fKCdTZXJ2ZXIgbmFtZTonKX1cbiAgICAgICAgICAgICAgICAgIDwvaDM+XG4gICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLWlucHV0RmllbGRXcmFwcGVyIGpwLUZvcm1Hcm91cC1jb250ZW50SXRlbVwiPlxuICAgICAgICAgICAgICAgICAgICA8aW5wdXRcbiAgICAgICAgICAgICAgICAgICAgICBjbGFzc05hbWU9XCJmb3JtLWNvbnRyb2xcIlxuICAgICAgICAgICAgICAgICAgICAgIHR5cGU9XCJ0ZXh0XCJcbiAgICAgICAgICAgICAgICAgICAgICByZXF1aXJlZD17dHJ1ZX1cbiAgICAgICAgICAgICAgICAgICAgICB2YWx1ZT17Y3VycmVudFNlcnZlck5hbWV9XG4gICAgICAgICAgICAgICAgICAgICAgb25DaGFuZ2U9e2UgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgb25TZXJ2ZXJOYW1lQ2hhbmdlKGUpO1xuICAgICAgICAgICAgICAgICAgICAgIH19XG4gICAgICAgICAgICAgICAgICAgIC8+XG4gICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwidmFsaWRhdGlvbkVycm9yc1wiPlxuICAgICAgICAgICAgICAgICAgICA8ZGl2PlxuICAgICAgICAgICAgICAgICAgICAgIDx1bCBjbGFzc05hbWU9XCJlcnJvci1kZXRhaWwgYnMtY2FsbG91dCBicy1jYWxsb3V0LWluZm9cIj5cbiAgICAgICAgICAgICAgICAgICAgICAgIDxsaSBjbGFzc05hbWU9XCJ0ZXh0LWRhbmdlclwiPlxuICAgICAgICAgICAgICAgICAgICAgICAgICB7cHJvcHMudHJhbnMuX18oJ2lzIGEgcmVxdWlyZWQgcHJvcGVydHknKX1cbiAgICAgICAgICAgICAgICAgICAgICAgIDwvbGk+XG4gICAgICAgICAgICAgICAgICAgICAgPC91bD5cbiAgICAgICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgIHtPYmplY3QuZW50cmllcyhvdGhlclNldHRpbmdzU2NoZW1hKS5tYXAoXG4gICAgICAgICAgICAgICAgKFtwcm9wZXJ0eSwgdmFsdWVdLCBpZHgpID0+IHtcbiAgICAgICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgICAgIDxkaXZcbiAgICAgICAgICAgICAgICAgICAgICBrZXk9e2Ake2lkeH0tJHtwcm9wZXJ0eX1gfVxuICAgICAgICAgICAgICAgICAgICAgIGNsYXNzTmFtZT1cImZvcm0tZ3JvdXAgc21hbGwtZmllbGRcIlxuICAgICAgICAgICAgICAgICAgICA+XG4gICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1Gb3JtR3JvdXAtY29udGVudFwiPlxuICAgICAgICAgICAgICAgICAgICAgICAgPGgzIGNsYXNzTmFtZT1cImpwLUZvcm1Hcm91cC1maWVsZExhYmVsIGpwLUZvcm1Hcm91cC1jb250ZW50SXRlbVwiPlxuICAgICAgICAgICAgICAgICAgICAgICAgICB7dmFsdWUudGl0bGV9XG4gICAgICAgICAgICAgICAgICAgICAgICA8L2gzPlxuICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzc05hbWU9XCJqcC1pbnB1dEZpZWxkV3JhcHBlciBqcC1Gb3JtR3JvdXAtY29udGVudEl0ZW1cIj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgPGlucHV0XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgY2xhc3NOYW1lPVwiZm9ybS1jb250cm9sXCJcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwbGFjZWhvbGRlcj1cIlwiXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdHlwZT17dmFsdWUudHlwZX1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB2YWx1ZT17b3RoZXJTZXR0aW5nc0NvbXBvc2l0ZVtwcm9wZXJ0eV19XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgb25DaGFuZ2U9e2UgPT5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG9uT3RoZXJTZXR0aW5nc0NoYW5nZShcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJvcGVydHksXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGUudGFyZ2V0LnZhbHVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB2YWx1ZS50eXBlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICApXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICAgICAgICAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUZvcm1Hcm91cC1kZXNjcmlwdGlvblwiPlxuICAgICAgICAgICAgICAgICAgICAgICAgICB7dmFsdWUuZGVzY3JpcHRpb259XG4gICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwidmFsaWRhdGlvbkVycm9yc1wiPjwvZGl2PlxuICAgICAgICAgICAgICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICApfVxuICAgICAgICAgICAgICA8ZmllbGRzZXQ+XG4gICAgICAgICAgICAgICAgPGxlZ2VuZD57c2VydmVyU2V0dGluZ3NTY2hlbWFbJ3RpdGxlJ119PC9sZWdlbmQ+XG4gICAgICAgICAgICAgICAge09iamVjdC5lbnRyaWVzKHByb3BlcnR5TWFwKS5tYXAoKFtoYXNoLCBwcm9wZXJ0eV0pID0+IHtcbiAgICAgICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgICAgIDxQcm9wZXJ0eUZyb21cbiAgICAgICAgICAgICAgICAgICAgICBrZXk9e2hhc2h9XG4gICAgICAgICAgICAgICAgICAgICAgaGFzaD17aGFzaH1cbiAgICAgICAgICAgICAgICAgICAgICBwcm9wZXJ0eT17cHJvcGVydHl9XG4gICAgICAgICAgICAgICAgICAgICAgcmVtb3ZlUHJvcGVydHk9e3JlbW92ZVByb3BlcnR5fVxuICAgICAgICAgICAgICAgICAgICAgIHNldFByb3BlcnR5PXtkZWJvdW5jZWRTZXRQcm9wZXJ0eX1cbiAgICAgICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgICAgICk7XG4gICAgICAgICAgICAgICAgfSl9XG4gICAgICAgICAgICAgICAgPHNwYW4+e3NlcnZlclNldHRpbmdzU2NoZW1hWydkZXNjcmlwdGlvbiddfTwvc3Bhbj5cbiAgICAgICAgICAgICAgPC9maWVsZHNldD5cbiAgICAgICAgICAgIDwvZmllbGRzZXQ+XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgIDwvZGl2PlxuICAgICAgPC9kaXY+XG4gICAgICA8ZGl2IGNsYXNzTmFtZT1cImpwLUFycmF5T3BlcmF0aW9uc1wiPlxuICAgICAgICA8YnV0dG9uIGNsYXNzTmFtZT1cImpwLW1vZC1zdHlsZWQganAtbW9kLXJlamVjdFwiIG9uQ2xpY2s9e2FkZFByb3BlcnR5fT5cbiAgICAgICAgICB7cHJvcHMudHJhbnMuX18oJ0FkZCBwcm9wZXJ0eScpfVxuICAgICAgICA8L2J1dHRvbj5cbiAgICAgICAgPGJ1dHRvblxuICAgICAgICAgIGNsYXNzTmFtZT1cImpwLW1vZC1zdHlsZWQganAtbW9kLXdhcm4ganAtRm9ybUdyb3VwLXJlbW92ZUJ1dHRvblwiXG4gICAgICAgICAgb25DbGljaz17KCkgPT4gcHJvcHMucmVtb3ZlU2V0dGluZyhwcm9wcy5zZXJ2ZXJIYXNoKX1cbiAgICAgICAgPlxuICAgICAgICAgIHtwcm9wcy50cmFucy5fXygnUmVtb3ZlIHNlcnZlcicpfVxuICAgICAgICA8L2J1dHRvbj5cbiAgICAgIDwvZGl2PlxuICAgIDwvZGl2PlxuICApO1xufVxuXG5mdW5jdGlvbiBQcm9wZXJ0eUZyb20ocHJvcHM6IHtcbiAgaGFzaDogc3RyaW5nO1xuICBwcm9wZXJ0eTogSVNldHRpbmdQcm9wZXJ0eTtcbiAgcmVtb3ZlUHJvcGVydHk6IChoYXNoOiBzdHJpbmcpID0+IHZvaWQ7XG4gIHNldFByb3BlcnR5OiBEZWJvdW5jZXI8dm9pZCwgYW55LCBbaGFzaDogc3RyaW5nLCBwcm9wZXJ0eTogSVNldHRpbmdQcm9wZXJ0eV0+O1xufSk6IEpTWC5FbGVtZW50IHtcbiAgY29uc3QgW3N0YXRlLCBzZXRTdGF0ZV0gPSB1c2VTdGF0ZTx7XG4gICAgcHJvcGVydHk6IHN0cmluZztcbiAgICB0eXBlOiAnYm9vbGVhbicgfCAnc3RyaW5nJyB8ICdudW1iZXInO1xuICAgIHZhbHVlOiBhbnk7XG4gIH0+KHsgLi4ucHJvcHMucHJvcGVydHkgfSk7XG4gIGNvbnN0IFRZUEVfTUFQID0geyBzdHJpbmc6ICd0ZXh0JywgbnVtYmVyOiAnbnVtYmVyJywgYm9vbGVhbjogJ2NoZWNrYm94JyB9O1xuXG4gIGNvbnN0IHJlbW92ZUl0ZW0gPSAoKSA9PiB7XG4gICAgcHJvcHMucmVtb3ZlUHJvcGVydHkocHJvcHMuaGFzaCk7XG4gIH07XG5cbiAgY29uc3QgY2hhbmdlTmFtZSA9IChuZXdOYW1lOiBzdHJpbmcpID0+IHtcbiAgICBjb25zdCBuZXdTdGF0ZSA9IHsgLi4uc3RhdGUsIHByb3BlcnR5OiBuZXdOYW1lIH07XG4gICAgcHJvcHMuc2V0UHJvcGVydHkuaW52b2tlKHByb3BzLmhhc2gsIG5ld1N0YXRlKS5jYXRjaChjb25zb2xlLmVycm9yKTtcbiAgICBzZXRTdGF0ZShuZXdTdGF0ZSk7XG4gIH07XG5cbiAgY29uc3QgY2hhbmdlVmFsdWUgPSAoXG4gICAgbmV3VmFsdWU6IGFueSxcbiAgICB0eXBlOiAnc3RyaW5nJyB8ICdib29sZWFuJyB8ICdudW1iZXInXG4gICkgPT4ge1xuICAgIGxldCB2YWx1ZSA9IG5ld1ZhbHVlO1xuICAgIGlmICh0eXBlID09PSAnbnVtYmVyJykge1xuICAgICAgdmFsdWUgPSBwYXJzZUZsb2F0KG5ld1ZhbHVlKTtcbiAgICB9XG4gICAgY29uc3QgbmV3U3RhdGUgPSB7IC4uLnN0YXRlLCB2YWx1ZSB9O1xuICAgIHByb3BzLnNldFByb3BlcnR5Lmludm9rZShwcm9wcy5oYXNoLCBuZXdTdGF0ZSkuY2F0Y2goY29uc29sZS5lcnJvcik7XG4gICAgc2V0U3RhdGUobmV3U3RhdGUpO1xuICB9O1xuXG4gIGNvbnN0IGNoYW5nZVR5cGUgPSAobmV3VHlwZTogJ2Jvb2xlYW4nIHwgJ3N0cmluZycgfCAnbnVtYmVyJykgPT4ge1xuICAgIGxldCB2YWx1ZTogc3RyaW5nIHwgYm9vbGVhbiB8IG51bWJlcjtcbiAgICBpZiAobmV3VHlwZSA9PT0gJ2Jvb2xlYW4nKSB7XG4gICAgICB2YWx1ZSA9IGZhbHNlO1xuICAgIH0gZWxzZSBpZiAobmV3VHlwZSA9PT0gJ251bWJlcicpIHtcbiAgICAgIHZhbHVlID0gMDtcbiAgICB9IGVsc2Uge1xuICAgICAgdmFsdWUgPSAnJztcbiAgICB9XG4gICAgY29uc3QgbmV3U3RhdGUgPSB7IC4uLnN0YXRlLCB0eXBlOiBuZXdUeXBlLCB2YWx1ZSB9O1xuICAgIHNldFN0YXRlKG5ld1N0YXRlKTtcbiAgICBwcm9wcy5zZXRQcm9wZXJ0eS5pbnZva2UocHJvcHMuaGFzaCwgbmV3U3RhdGUpLmNhdGNoKGNvbnNvbGUuZXJyb3IpO1xuICB9O1xuXG4gIHJldHVybiAoXG4gICAgPGRpdiBrZXk9e3Byb3BzLmhhc2h9IGNsYXNzTmFtZT1cImZvcm0tZ3JvdXAgc21hbGwtZmllbGRcIj5cbiAgICAgIDxkaXYgY2xhc3NOYW1lPVwianAtRm9ybUdyb3VwLWNvbnRlbnQganAtTFNQRXh0ZW5zaW9uLUZvcm1Hcm91cC1jb250ZW50XCI+XG4gICAgICAgIDxpbnB1dFxuICAgICAgICAgIGNsYXNzTmFtZT1cImZvcm0tY29udHJvbFwiXG4gICAgICAgICAgdHlwZT1cInRleHRcIlxuICAgICAgICAgIHJlcXVpcmVkPXt0cnVlfVxuICAgICAgICAgIHBsYWNlaG9sZGVyPXsnUHJvcGVydHkgbmFtZSd9XG4gICAgICAgICAgdmFsdWU9e3N0YXRlLnByb3BlcnR5fVxuICAgICAgICAgIG9uQ2hhbmdlPXtlID0+IHtcbiAgICAgICAgICAgIGNoYW5nZU5hbWUoZS50YXJnZXQudmFsdWUpO1xuICAgICAgICAgIH19XG4gICAgICAgIC8+XG4gICAgICAgIDxzZWxlY3RcbiAgICAgICAgICBjbGFzc05hbWU9XCJmb3JtLWNvbnRyb2xcIlxuICAgICAgICAgIHZhbHVlPXtzdGF0ZS50eXBlfVxuICAgICAgICAgIG9uQ2hhbmdlPXtlID0+XG4gICAgICAgICAgICBjaGFuZ2VUeXBlKGUudGFyZ2V0LnZhbHVlIGFzICdib29sZWFuJyB8ICdzdHJpbmcnIHwgJ251bWJlcicpXG4gICAgICAgICAgfVxuICAgICAgICA+XG4gICAgICAgICAgPG9wdGlvbiB2YWx1ZT1cInN0cmluZ1wiPlN0cmluZzwvb3B0aW9uPlxuICAgICAgICAgIDxvcHRpb24gdmFsdWU9XCJudW1iZXJcIj5OdW1iZXI8L29wdGlvbj5cbiAgICAgICAgICA8b3B0aW9uIHZhbHVlPVwiYm9vbGVhblwiPkJvb2xlYW48L29wdGlvbj5cbiAgICAgICAgPC9zZWxlY3Q+XG4gICAgICAgIDxpbnB1dFxuICAgICAgICAgIGNsYXNzTmFtZT1cImZvcm0tY29udHJvbFwiXG4gICAgICAgICAgdHlwZT17VFlQRV9NQVBbc3RhdGUudHlwZV19XG4gICAgICAgICAgcmVxdWlyZWQ9e2ZhbHNlfVxuICAgICAgICAgIHBsYWNlaG9sZGVyPXsnUHJvcGVydHkgdmFsdWUnfVxuICAgICAgICAgIHZhbHVlPXtzdGF0ZS50eXBlICE9PSAnYm9vbGVhbicgPyBzdGF0ZS52YWx1ZSA6IHVuZGVmaW5lZH1cbiAgICAgICAgICBjaGVja2VkPXtzdGF0ZS50eXBlID09PSAnYm9vbGVhbicgPyBzdGF0ZS52YWx1ZSA6IHVuZGVmaW5lZH1cbiAgICAgICAgICBvbkNoYW5nZT17XG4gICAgICAgICAgICBzdGF0ZS50eXBlICE9PSAnYm9vbGVhbidcbiAgICAgICAgICAgICAgPyBlID0+IGNoYW5nZVZhbHVlKGUudGFyZ2V0LnZhbHVlLCBzdGF0ZS50eXBlKVxuICAgICAgICAgICAgICA6IGUgPT4gY2hhbmdlVmFsdWUoZS50YXJnZXQuY2hlY2tlZCwgc3RhdGUudHlwZSlcbiAgICAgICAgICB9XG4gICAgICAgIC8+XG4gICAgICAgIDxidXR0b24gY2xhc3NOYW1lPVwianAtbW9kLW1pbmltYWwganAtQnV0dG9uXCIgb25DbGljaz17cmVtb3ZlSXRlbX0+XG4gICAgICAgICAgPGNsb3NlSWNvbi5yZWFjdCAvPlxuICAgICAgICA8L2J1dHRvbj5cbiAgICAgIDwvZGl2PlxuICAgIDwvZGl2PlxuICApO1xufVxuXG4vKipcbiAqIEludGVybmFsIHN0YXRlIG9mIHRoZSBzZXR0aW5nIGNvbXBvbmVudFxuICovXG5pbnRlcmZhY2UgSVN0YXRlIHtcbiAgLyoqXG4gICAqIFRpdGxlIG9mIHRoZSBzZXR0aW5nIHNlY3Rpb25cbiAgICovXG4gIHRpdGxlPzogc3RyaW5nO1xuICAvKipcbiAgICogRGVzY3JpcHRpb24gb2YgdGhlIHNldHRpbmcgc2VjdGlvblxuICAgKi9cbiAgZGVzYz86IHN0cmluZztcbiAgLyoqXG4gICAqIEl0ZW1zIG9mIHNldHRpbmcgc2VjdGlvblxuICAgKi9cbiAgaXRlbXM6IFREaWN0O1xufVxuaW50ZXJmYWNlIElQcm9wcyBleHRlbmRzIEZpZWxkUHJvcHMge1xuICB0cmFuc2xhdG9yOiBJVHJhbnNsYXRvcjtcbn1cblxuLyoqXG4gKiBSZWFjdCBzZXR0aW5nIGNvbXBvbmVudFxuICovXG5jbGFzcyBTZXR0aW5nUmVuZGVyZXIgZXh0ZW5kcyBSZWFjdC5Db21wb25lbnQ8SVByb3BzLCBJU3RhdGU+IHtcbiAgY29uc3RydWN0b3IocHJvcHM6IElQcm9wcykge1xuICAgIHN1cGVyKHByb3BzKTtcbiAgICB0aGlzLl9zZXR0aW5nID0gcHJvcHMuZm9ybUNvbnRleHQuc2V0dGluZ3M7XG4gICAgdGhpcy5fdHJhbnMgPSBwcm9wcy50cmFuc2xhdG9yLmxvYWQoJ2p1cHl0ZXJsYWInKTtcblxuICAgIGNvbnN0IHNjaGVtYSA9IHRoaXMuX3NldHRpbmcuc2NoZW1hWydkZWZpbml0aW9ucyddIGFzIFREaWN0O1xuXG4gICAgdGhpcy5fZGVmYXVsdFNldHRpbmcgPSBzY2hlbWFbJ2xhbmd1YWdlU2VydmVyJ11bJ2RlZmF1bHQnXTtcbiAgICB0aGlzLl9zY2hlbWEgPSBzY2hlbWFbJ2xhbmd1YWdlU2VydmVyJ11bJ3Byb3BlcnRpZXMnXTtcbiAgICBjb25zdCB0aXRsZSA9IHByb3BzLnNjaGVtYS50aXRsZTtcbiAgICBjb25zdCBkZXNjID0gcHJvcHMuc2NoZW1hLmRlc2NyaXB0aW9uO1xuICAgIGNvbnN0IHNldHRpbmdzOiBJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncyA9IHByb3BzLmZvcm1Db250ZXh0LnNldHRpbmdzO1xuICAgIGNvbnN0IGNvbXBvc2l0ZURhdGEgPSBzZXR0aW5ncy5nZXQoU0VUVElOR19OQU1FKS5jb21wb3NpdGUgYXMgVERpY3Q7XG5cbiAgICBsZXQgaXRlbXM6IFREaWN0ID0ge307XG4gICAgaWYgKGNvbXBvc2l0ZURhdGEpIHtcbiAgICAgIE9iamVjdC5lbnRyaWVzKGNvbXBvc2l0ZURhdGEpLmZvckVhY2goKFtrZXksIHZhbHVlXSkgPT4ge1xuICAgICAgICBpZiAodmFsdWUpIHtcbiAgICAgICAgICBjb25zdCBoYXNoID0gVVVJRC51dWlkNCgpO1xuICAgICAgICAgIGl0ZW1zW2hhc2hdID0geyBzZXJ2ZXJOYW1lOiBrZXksIC4uLnZhbHVlIH07XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICAgIH1cbiAgICB0aGlzLnN0YXRlID0geyB0aXRsZSwgZGVzYywgaXRlbXMgfTtcbiAgICB0aGlzLl9kZWJvdW5jZWRVcGRhdGVTZXR0aW5nID0gbmV3IERlYm91bmNlcih0aGlzLnVwZGF0ZVNldHRpbmcuYmluZCh0aGlzKSk7XG4gIH1cblxuICAvKipcbiAgICogUmVtb3ZlIGEgc2V0dGluZyBpdGVtIGJ5IGl0cyBoYXNoXG4gICAqXG4gICAqIEBwYXJhbSBoYXNoIC0gaGFzaCBvZiB0aGUgaXRlbSB0byBiZSByZW1vdmVkLlxuICAgKi9cbiAgcmVtb3ZlU2V0dGluZyA9IChoYXNoOiBzdHJpbmcpOiB2b2lkID0+IHtcbiAgICBpZiAoaGFzaCBpbiB0aGlzLnN0YXRlLml0ZW1zKSB7XG4gICAgICBjb25zdCBpdGVtczogVERpY3QgPSB7fTtcbiAgICAgIGZvciAoY29uc3Qga2V5IGluIHRoaXMuc3RhdGUuaXRlbXMpIHtcbiAgICAgICAgaWYgKGtleSAhPT0gaGFzaCkge1xuICAgICAgICAgIGl0ZW1zW2tleV0gPSB0aGlzLnN0YXRlLml0ZW1zW2tleV07XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICAgIHRoaXMuc2V0U3RhdGUoXG4gICAgICAgIG9sZCA9PiB7XG4gICAgICAgICAgcmV0dXJuIHsgLi4ub2xkLCBpdGVtcyB9O1xuICAgICAgICB9LFxuICAgICAgICAoKSA9PiB7XG4gICAgICAgICAgdGhpcy5zYXZlU2VydmVyU2V0dGluZygpO1xuICAgICAgICB9XG4gICAgICApO1xuICAgIH1cbiAgfTtcblxuICAvKipcbiAgICogVXBkYXRlIGEgc2V0dGluZyBpdGVtIGJ5IGl0cyBoYXNoXG4gICAqXG4gICAqIEBwYXJhbSBoYXNoIC0gaGFzaCBvZiB0aGUgaXRlbSB0byBiZSB1cGRhdGVkLlxuICAgKiBAcGFyYW0gbmV3U2V0dGluZyAtIG5ldyBzZXR0aW5nIHZhbHVlLlxuICAgKi9cbiAgdXBkYXRlU2V0dGluZyA9IChoYXNoOiBzdHJpbmcsIG5ld1NldHRpbmc6IFREaWN0KTogdm9pZCA9PiB7XG4gICAgaWYgKGhhc2ggaW4gdGhpcy5zdGF0ZS5pdGVtcykge1xuICAgICAgY29uc3QgaXRlbXM6IFREaWN0ID0ge307XG4gICAgICBmb3IgKGNvbnN0IGtleSBpbiB0aGlzLnN0YXRlLml0ZW1zKSB7XG4gICAgICAgIGlmIChrZXkgPT09IGhhc2gpIHtcbiAgICAgICAgICBpdGVtc1trZXldID0geyAuLi50aGlzLnN0YXRlLml0ZW1zW2tleV0sIC4uLm5ld1NldHRpbmcgfTtcbiAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICBpdGVtc1trZXldID0gdGhpcy5zdGF0ZS5pdGVtc1trZXldO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgICB0aGlzLnNldFN0YXRlKFxuICAgICAgICBvbGQgPT4ge1xuICAgICAgICAgIHJldHVybiB7IC4uLm9sZCwgaXRlbXMgfTtcbiAgICAgICAgfSxcbiAgICAgICAgKCkgPT4ge1xuICAgICAgICAgIHRoaXMuc2F2ZVNlcnZlclNldHRpbmcoKTtcbiAgICAgICAgfVxuICAgICAgKTtcbiAgICB9XG4gIH07XG5cbiAgLyoqXG4gICAqIEFkZCBzZXR0aW5nIGl0ZW0gdG8gdGhlIHNldHRpbmcgY29tcG9uZW50LlxuICAgKi9cbiAgYWRkU2VydmVyU2V0dGluZyA9ICgpOiB2b2lkID0+IHtcbiAgICBsZXQgaW5kZXggPSAwO1xuICAgIGxldCBrZXkgPSAnbmV3S2V5JztcbiAgICB3aGlsZSAoXG4gICAgICBPYmplY3QudmFsdWVzKHRoaXMuc3RhdGUuaXRlbXMpXG4gICAgICAgIC5tYXAodmFsID0+IHZhbC5zZXJ2ZXJOYW1lKVxuICAgICAgICAuaW5jbHVkZXMoa2V5KVxuICAgICkge1xuICAgICAgaW5kZXggKz0gMTtcbiAgICAgIGtleSA9IGBuZXdLZXktJHtpbmRleH1gO1xuICAgIH1cbiAgICB0aGlzLnNldFN0YXRlKFxuICAgICAgb2xkID0+ICh7XG4gICAgICAgIC4uLm9sZCxcbiAgICAgICAgaXRlbXM6IHtcbiAgICAgICAgICAuLi5vbGQuaXRlbXMsXG4gICAgICAgICAgW1VVSUQudXVpZDQoKV06IHsgLi4udGhpcy5fZGVmYXVsdFNldHRpbmcsIHNlcnZlck5hbWU6IGtleSB9XG4gICAgICAgIH1cbiAgICAgIH0pLFxuICAgICAgKCkgPT4ge1xuICAgICAgICB0aGlzLnNhdmVTZXJ2ZXJTZXR0aW5nKCk7XG4gICAgICB9XG4gICAgKTtcbiAgfTtcblxuICAvKipcbiAgICogU2F2ZSB0aGUgdmFsdWUgb2Ygc2V0dGluZyBpdGVtcyB0byB0aGUgc2V0dGluZyByZWdpc3RyeS5cbiAgICovXG4gIHNhdmVTZXJ2ZXJTZXR0aW5nID0gKCkgPT4ge1xuICAgIGNvbnN0IHNldHRpbmdzOiBURGljdCA9IHt9O1xuICAgIE9iamVjdC52YWx1ZXModGhpcy5zdGF0ZS5pdGVtcykuZm9yRWFjaChpdGVtID0+IHtcbiAgICAgIGNvbnN0IHsgc2VydmVyTmFtZSwgLi4uc2V0dGluZyB9ID0gaXRlbTtcbiAgICAgIHNldHRpbmdzW3NlcnZlck5hbWVdID0gc2V0dGluZztcbiAgICB9KTtcbiAgICB0aGlzLl9zZXR0aW5nLnNldChTRVRUSU5HX05BTUUsIHNldHRpbmdzKS5jYXRjaChjb25zb2xlLmVycm9yKTtcbiAgfTtcbiAgcmVuZGVyKCk6IEpTWC5FbGVtZW50IHtcbiAgICByZXR1cm4gKFxuICAgICAgPGRpdj5cbiAgICAgICAgPGZpZWxkc2V0PlxuICAgICAgICAgIDxsZWdlbmQ+e3RoaXMuc3RhdGUudGl0bGV9PC9sZWdlbmQ+XG4gICAgICAgICAgPHAgY2xhc3NOYW1lPVwiZmllbGQtZGVzY3JpcHRpb25cIj57dGhpcy5zdGF0ZS5kZXNjfTwvcD5cbiAgICAgICAgICA8ZGl2IGNsYXNzTmFtZT1cImZpZWxkIGZpZWxkLWFycmF5IGZpZWxkLWFycmF5LW9mLW9iamVjdFwiPlxuICAgICAgICAgICAge09iamVjdC5lbnRyaWVzKHRoaXMuc3RhdGUuaXRlbXMpLm1hcCgoW2hhc2gsIHZhbHVlXSwgaWR4KSA9PiB7XG4gICAgICAgICAgICAgIHJldHVybiAoXG4gICAgICAgICAgICAgICAgPEJ1aWxkU2V0dGluZ0Zvcm1cbiAgICAgICAgICAgICAgICAgIGtleT17YCR7aWR4fS0ke2hhc2h9YH1cbiAgICAgICAgICAgICAgICAgIHRyYW5zPXt0aGlzLl90cmFuc31cbiAgICAgICAgICAgICAgICAgIHJlbW92ZVNldHRpbmc9e3RoaXMucmVtb3ZlU2V0dGluZ31cbiAgICAgICAgICAgICAgICAgIHVwZGF0ZVNldHRpbmc9e3RoaXMuX2RlYm91bmNlZFVwZGF0ZVNldHRpbmd9XG4gICAgICAgICAgICAgICAgICBzZXJ2ZXJIYXNoPXtoYXNofVxuICAgICAgICAgICAgICAgICAgc2V0dGluZ3M9e3ZhbHVlfVxuICAgICAgICAgICAgICAgICAgc2NoZW1hPXt0aGlzLl9zY2hlbWF9XG4gICAgICAgICAgICAgICAgLz5cbiAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIH0pfVxuICAgICAgICAgIDwvZGl2PlxuICAgICAgICAgIDxkaXY+XG4gICAgICAgICAgICA8YnV0dG9uXG4gICAgICAgICAgICAgIHN0eWxlPXt7IG1hcmdpbjogMiB9fVxuICAgICAgICAgICAgICBjbGFzc05hbWU9XCJqcC1tb2Qtc3R5bGVkIGpwLW1vZC1yZWplY3RcIlxuICAgICAgICAgICAgICBvbkNsaWNrPXt0aGlzLmFkZFNlcnZlclNldHRpbmd9XG4gICAgICAgICAgICA+XG4gICAgICAgICAgICAgIHt0aGlzLl90cmFucy5fXygnQWRkIHNlcnZlcicpfVxuICAgICAgICAgICAgPC9idXR0b24+XG4gICAgICAgICAgPC9kaXY+XG4gICAgICAgIDwvZmllbGRzZXQ+XG4gICAgICA8L2Rpdj5cbiAgICApO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBzZXR0aW5nIHJlZ2lzdHJ5LlxuICAgKi9cbiAgcHJpdmF0ZSBfc2V0dGluZzogSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3M7XG5cbiAgLyoqXG4gICAqIFRoZSB0cmFuc2xhdGlvbiBidW5kbGUuXG4gICAqL1xuICBwcml2YXRlIF90cmFuczogVHJhbnNsYXRpb25CdW5kbGU7XG5cbiAgLyoqXG4gICAqIERlZmF1bHQgc2V0dGluZyB2YWx1ZS5cbiAgICovXG4gIHByaXZhdGUgX2RlZmF1bHRTZXR0aW5nOiBURGljdDtcblxuICAvKipcbiAgICogVGhlIHNldHRpbmcgc2NoZW1hLlxuICAgKi9cbiAgcHJpdmF0ZSBfc2NoZW1hOiBURGljdDtcblxuICBwcml2YXRlIF9kZWJvdW5jZWRVcGRhdGVTZXR0aW5nOiBEZWJvdW5jZXI8XG4gICAgdm9pZCxcbiAgICBhbnksXG4gICAgW2hhc2g6IHN0cmluZywgbmV3U2V0dGluZzogVERpY3RdXG4gID47XG59XG5cbi8qKlxuICogQ3VzdG9tIHNldHRpbmcgcmVuZGVyZXIgZm9yIGxhbmd1YWdlIHNlcnZlciBleHRlbnNpb24uXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiByZW5kZXJTZXJ2ZXJTZXR0aW5nKFxuICBwcm9wczogRmllbGRQcm9wcyxcbiAgdHJhbnNsYXRvcjogSVRyYW5zbGF0b3Jcbik6IEpTWC5FbGVtZW50IHtcbiAgcmV0dXJuIDxTZXR0aW5nUmVuZGVyZXIgey4uLnByb3BzfSB0cmFuc2xhdG9yPXt0cmFuc2xhdG9yfSAvPjtcbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==