"use strict";
(self["webpackChunk_jupyterlab_application_top"] = self["webpackChunk_jupyterlab_application_top"] || []).push([["packages_settingregistry_lib_index_js"],{

/***/ "../../packages/settingregistry/lib/index.js":
/*!***************************************************!*\
  !*** ../../packages/settingregistry/lib/index.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DefaultSchemaValidator": () => (/* reexport safe */ _settingregistry__WEBPACK_IMPORTED_MODULE_0__.DefaultSchemaValidator),
/* harmony export */   "ISettingRegistry": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_1__.ISettingRegistry),
/* harmony export */   "SettingRegistry": () => (/* reexport safe */ _settingregistry__WEBPACK_IMPORTED_MODULE_0__.SettingRegistry),
/* harmony export */   "Settings": () => (/* reexport safe */ _settingregistry__WEBPACK_IMPORTED_MODULE_0__.Settings)
/* harmony export */ });
/* harmony import */ var _settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./settingregistry */ "../../packages/settingregistry/lib/settingregistry.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./tokens */ "../../packages/settingregistry/lib/tokens.js");
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
/**
 * @packageDocumentation
 * @module settingregistry
 */




/***/ }),

/***/ "../../packages/settingregistry/lib/settingregistry.js":
/*!*************************************************************!*\
  !*** ../../packages/settingregistry/lib/settingregistry.js ***!
  \*************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "DefaultSchemaValidator": () => (/* binding */ DefaultSchemaValidator),
/* harmony export */   "SettingRegistry": () => (/* binding */ SettingRegistry),
/* harmony export */   "Settings": () => (/* binding */ Settings)
/* harmony export */ });
/* harmony import */ var _lumino_commands__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/commands */ "webpack/sharing/consume/default/@lumino/commands/@lumino/commands");
/* harmony import */ var _lumino_commands__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_commands__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var ajv__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ajv */ "../../node_modules/ajv/lib/ajv.js");
/* harmony import */ var ajv__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(ajv__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var json5__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! json5 */ "../../node_modules/json5/dist/index.js");
/* harmony import */ var json5__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(json5__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _plugin_schema_json__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./plugin-schema.json */ "../../packages/settingregistry/lib/plugin-schema.json");
// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.







/**
 * An alias for the JSON deep copy function.
 */
const copy = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy;
/**
 * The default number of milliseconds before a `load()` call to the registry
 * will wait before timing out if it requires a transformation that has not been
 * registered.
 */
const DEFAULT_TRANSFORM_TIMEOUT = 1000;
/**
 * The ASCII record separator character.
 */
const RECORD_SEPARATOR = String.fromCharCode(30);
/**
 * The default implementation of a schema validator.
 */
class DefaultSchemaValidator {
    /**
     * Instantiate a schema validator.
     */
    constructor() {
        this._composer = new (ajv__WEBPACK_IMPORTED_MODULE_4___default())({ useDefaults: true });
        this._validator = new (ajv__WEBPACK_IMPORTED_MODULE_4___default())();
        this._composer.addSchema(_plugin_schema_json__WEBPACK_IMPORTED_MODULE_6__, 'jupyterlab-plugin-schema');
        this._validator.addSchema(_plugin_schema_json__WEBPACK_IMPORTED_MODULE_6__, 'jupyterlab-plugin-schema');
    }
    /**
     * Validate a plugin's schema and user data; populate the `composite` data.
     *
     * @param plugin - The plugin being validated. Its `composite` data will be
     * populated by reference.
     *
     * @param populate - Whether plugin data should be populated, defaults to
     * `true`.
     *
     * @returns A list of errors if either the schema or data fail to validate or
     * `null` if there are no errors.
     */
    validateData(plugin, populate = true) {
        const validate = this._validator.getSchema(plugin.id);
        const compose = this._composer.getSchema(plugin.id);
        // If the schemas do not exist, add them to the validator and continue.
        if (!validate || !compose) {
            if (plugin.schema.type !== 'object') {
                const keyword = 'schema';
                const message = `Setting registry schemas' root-level type must be ` +
                    `'object', rejecting type: ${plugin.schema.type}`;
                return [{ dataPath: 'type', keyword, schemaPath: '', message }];
            }
            const errors = this._addSchema(plugin.id, plugin.schema);
            return errors || this.validateData(plugin);
        }
        // Parse the raw commented JSON into a user map.
        let user;
        try {
            user = json5__WEBPACK_IMPORTED_MODULE_5__.parse(plugin.raw);
        }
        catch (error) {
            if (error instanceof SyntaxError) {
                return [
                    {
                        dataPath: '',
                        keyword: 'syntax',
                        schemaPath: '',
                        message: error.message
                    }
                ];
            }
            const { column, description } = error;
            const line = error.lineNumber;
            return [
                {
                    dataPath: '',
                    keyword: 'parse',
                    schemaPath: '',
                    message: `${description} (line ${line} column ${column})`
                }
            ];
        }
        if (!validate(user)) {
            return validate.errors;
        }
        // Copy the user data before merging defaults into composite map.
        const composite = copy(user);
        if (!compose(composite)) {
            return compose.errors;
        }
        if (populate) {
            plugin.data = { composite, user };
        }
        return null;
    }
    /**
     * Add a schema to the validator.
     *
     * @param plugin - The plugin ID.
     *
     * @param schema - The schema being added.
     *
     * @returns A list of errors if the schema fails to validate or `null` if there
     * are no errors.
     *
     * #### Notes
     * It is safe to call this function multiple times with the same plugin name.
     */
    _addSchema(plugin, schema) {
        const composer = this._composer;
        const validator = this._validator;
        const validate = validator.getSchema('jupyterlab-plugin-schema');
        // Validate against the main schema.
        if (!validate(schema)) {
            return validate.errors;
        }
        // Validate against the JSON schema meta-schema.
        if (!validator.validateSchema(schema)) {
            return validator.errors;
        }
        // Remove if schema already exists.
        composer.removeSchema(plugin);
        validator.removeSchema(plugin);
        // Add schema to the validator and composer.
        composer.addSchema(schema, plugin);
        validator.addSchema(schema, plugin);
        return null;
    }
}
/**
 * The default concrete implementation of a setting registry.
 */
class SettingRegistry {
    /**
     * Create a new setting registry.
     */
    constructor(options) {
        /**
         * The schema of the setting registry.
         */
        this.schema = _plugin_schema_json__WEBPACK_IMPORTED_MODULE_6__;
        /**
         * The collection of setting registry plugins.
         */
        this.plugins = Object.create(null);
        this._pluginChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
        this._ready = Promise.resolve();
        this._transformers = Object.create(null);
        this.connector = options.connector;
        this.validator = options.validator || new DefaultSchemaValidator();
        this._timeout = options.timeout || DEFAULT_TRANSFORM_TIMEOUT;
        // Preload with any available data at instantiation-time.
        if (options.plugins) {
            this._ready = this._preload(options.plugins);
        }
    }
    /**
     * A signal that emits the name of a plugin when its settings change.
     */
    get pluginChanged() {
        return this._pluginChanged;
    }
    /**
     * Get an individual setting.
     *
     * @param plugin - The name of the plugin whose settings are being retrieved.
     *
     * @param key - The name of the setting being retrieved.
     *
     * @returns A promise that resolves when the setting is retrieved.
     */
    async get(plugin, key) {
        // Wait for data preload before allowing normal operation.
        await this._ready;
        const plugins = this.plugins;
        if (plugin in plugins) {
            const { composite, user } = plugins[plugin].data;
            return {
                composite: composite[key] !== undefined ? copy(composite[key]) : undefined,
                user: user[key] !== undefined ? copy(user[key]) : undefined
            };
        }
        return this.load(plugin).then(() => this.get(plugin, key));
    }
    /**
     * Load a plugin's settings into the setting registry.
     *
     * @param plugin - The name of the plugin whose settings are being loaded.
     *
     * @returns A promise that resolves with a plugin settings object or rejects
     * if the plugin is not found.
     */
    async load(plugin) {
        // Wait for data preload before allowing normal operation.
        await this._ready;
        const plugins = this.plugins;
        const registry = this; // eslint-disable-line
        // If the plugin exists, resolve.
        if (plugin in plugins) {
            return new Settings({ plugin: plugins[plugin], registry });
        }
        // If the plugin needs to be loaded from the data connector, fetch.
        return this.reload(plugin);
    }
    /**
     * Reload a plugin's settings into the registry even if they already exist.
     *
     * @param plugin - The name of the plugin whose settings are being reloaded.
     *
     * @returns A promise that resolves with a plugin settings object or rejects
     * with a list of `ISchemaValidator.IError` objects if it fails.
     */
    async reload(plugin) {
        // Wait for data preload before allowing normal operation.
        await this._ready;
        const fetched = await this.connector.fetch(plugin);
        const plugins = this.plugins; // eslint-disable-line
        const registry = this; // eslint-disable-line
        if (fetched === undefined) {
            throw [
                {
                    dataPath: '',
                    keyword: 'id',
                    message: `Could not fetch settings for ${plugin}.`,
                    schemaPath: ''
                }
            ];
        }
        await this._load(await this._transform('fetch', fetched));
        this._pluginChanged.emit(plugin);
        return new Settings({ plugin: plugins[plugin], registry });
    }
    /**
     * Remove a single setting in the registry.
     *
     * @param plugin - The name of the plugin whose setting is being removed.
     *
     * @param key - The name of the setting being removed.
     *
     * @returns A promise that resolves when the setting is removed.
     */
    async remove(plugin, key) {
        // Wait for data preload before allowing normal operation.
        await this._ready;
        const plugins = this.plugins;
        if (!(plugin in plugins)) {
            return;
        }
        const raw = json5__WEBPACK_IMPORTED_MODULE_5__.parse(plugins[plugin].raw);
        // Delete both the value and any associated comment.
        delete raw[key];
        delete raw[`// ${key}`];
        plugins[plugin].raw = Private.annotatedPlugin(plugins[plugin], raw);
        return this._save(plugin);
    }
    /**
     * Set a single setting in the registry.
     *
     * @param plugin - The name of the plugin whose setting is being set.
     *
     * @param key - The name of the setting being set.
     *
     * @param value - The value of the setting being set.
     *
     * @returns A promise that resolves when the setting has been saved.
     *
     */
    async set(plugin, key, value) {
        // Wait for data preload before allowing normal operation.
        await this._ready;
        const plugins = this.plugins;
        if (!(plugin in plugins)) {
            return this.load(plugin).then(() => this.set(plugin, key, value));
        }
        // Parse the raw JSON string removing all comments and return an object.
        const raw = json5__WEBPACK_IMPORTED_MODULE_5__.parse(plugins[plugin].raw);
        plugins[plugin].raw = Private.annotatedPlugin(plugins[plugin], Object.assign(Object.assign({}, raw), { [key]: value }));
        return this._save(plugin);
    }
    /**
     * Register a plugin transform function to act on a specific plugin.
     *
     * @param plugin - The name of the plugin whose settings are transformed.
     *
     * @param transforms - The transform functions applied to the plugin.
     *
     * @returns A disposable that removes the transforms from the registry.
     *
     * #### Notes
     * - `compose` transformations: The registry automatically overwrites a
     * plugin's default values with user overrides, but a plugin may instead wish
     * to merge values. This behavior can be accomplished in a `compose`
     * transformation.
     * - `fetch` transformations: The registry uses the plugin data that is
     * fetched from its connector. If a plugin wants to override, e.g. to update
     * its schema with dynamic defaults, a `fetch` transformation can be applied.
     */
    transform(plugin, transforms) {
        const transformers = this._transformers;
        if (plugin in transformers) {
            const error = new Error(`${plugin} already has a transformer.`);
            error.name = 'TransformError';
            throw error;
        }
        transformers[plugin] = {
            fetch: transforms.fetch || (plugin => plugin),
            compose: transforms.compose || (plugin => plugin)
        };
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_2__.DisposableDelegate(() => {
            delete transformers[plugin];
        });
    }
    /**
     * Upload a plugin's settings.
     *
     * @param plugin - The name of the plugin whose settings are being set.
     *
     * @param raw - The raw plugin settings being uploaded.
     *
     * @returns A promise that resolves when the settings have been saved.
     */
    async upload(plugin, raw) {
        // Wait for data preload before allowing normal operation.
        await this._ready;
        const plugins = this.plugins;
        if (!(plugin in plugins)) {
            return this.load(plugin).then(() => this.upload(plugin, raw));
        }
        // Set the local copy.
        plugins[plugin].raw = raw;
        return this._save(plugin);
    }
    /**
     * Load a plugin into the registry.
     */
    async _load(data) {
        const plugin = data.id;
        // Validate and preload the item.
        try {
            await this._validate(data);
        }
        catch (errors) {
            const output = [`Validating ${plugin} failed:`];
            errors.forEach((error, index) => {
                const { dataPath, schemaPath, keyword, message } = error;
                if (dataPath || schemaPath) {
                    output.push(`${index} - schema @ ${schemaPath}, data @ ${dataPath}`);
                }
                output.push(`{${keyword}} ${message}`);
            });
            console.warn(output.join('\n'));
            throw errors;
        }
    }
    /**
     * Preload a list of plugins and fail gracefully.
     */
    async _preload(plugins) {
        await Promise.all(plugins.map(async (plugin) => {
            var _a;
            try {
                // Apply a transformation to the plugin if necessary.
                await this._load(await this._transform('fetch', plugin));
            }
            catch (errors) {
                /* Ignore preload timeout errors silently. */
                if (((_a = errors[0]) === null || _a === void 0 ? void 0 : _a.keyword) !== 'timeout') {
                    console.warn('Ignored setting registry preload errors.', errors);
                }
            }
        }));
    }
    /**
     * Save a plugin in the registry.
     */
    async _save(plugin) {
        const plugins = this.plugins;
        if (!(plugin in plugins)) {
            throw new Error(`${plugin} does not exist in setting registry.`);
        }
        try {
            await this._validate(plugins[plugin]);
        }
        catch (errors) {
            console.warn(`${plugin} validation errors:`, errors);
            throw new Error(`${plugin} failed to validate; check console.`);
        }
        await this.connector.save(plugin, plugins[plugin].raw);
        // Fetch and reload the data to guarantee server and client are in sync.
        const fetched = await this.connector.fetch(plugin);
        if (fetched === undefined) {
            throw [
                {
                    dataPath: '',
                    keyword: 'id',
                    message: `Could not fetch settings for ${plugin}.`,
                    schemaPath: ''
                }
            ];
        }
        await this._load(await this._transform('fetch', fetched));
        this._pluginChanged.emit(plugin);
    }
    /**
     * Transform the plugin if necessary.
     */
    async _transform(phase, plugin, started = new Date().getTime()) {
        const elapsed = new Date().getTime() - started;
        const id = plugin.id;
        const transformers = this._transformers;
        const timeout = this._timeout;
        if (!plugin.schema['jupyter.lab.transform']) {
            return plugin;
        }
        if (id in transformers) {
            const transformed = transformers[id][phase].call(null, plugin);
            if (transformed.id !== id) {
                throw [
                    {
                        dataPath: '',
                        keyword: 'id',
                        message: 'Plugin transformations cannot change plugin IDs.',
                        schemaPath: ''
                    }
                ];
            }
            return transformed;
        }
        // If the timeout has not been exceeded, stall and try again in 250ms.
        if (elapsed < timeout) {
            await new Promise(resolve => {
                setTimeout(() => {
                    resolve();
                }, 250);
            });
            return this._transform(phase, plugin, started);
        }
        throw [
            {
                dataPath: '',
                keyword: 'timeout',
                message: `Transforming ${plugin.id} timed out.`,
                schemaPath: ''
            }
        ];
    }
    /**
     * Validate and preload a plugin, compose the `composite` data.
     */
    async _validate(plugin) {
        // Validate the user data and create the composite data.
        const errors = this.validator.validateData(plugin);
        if (errors) {
            throw errors;
        }
        // Apply a transformation if necessary and set the local copy.
        this.plugins[plugin.id] = await this._transform('compose', plugin);
    }
}
/**
 * A manager for a specific plugin's settings.
 */
class Settings {
    /**
     * Instantiate a new plugin settings manager.
     */
    constructor(options) {
        this._changed = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal(this);
        this._isDisposed = false;
        this.id = options.plugin.id;
        this.registry = options.registry;
        this.registry.pluginChanged.connect(this._onPluginChanged, this);
    }
    /**
     * A signal that emits when the plugin's settings have changed.
     */
    get changed() {
        return this._changed;
    }
    /**
     * The composite of user settings and extension defaults.
     */
    get composite() {
        return this.plugin.data.composite;
    }
    /**
     * Test whether the plugin settings manager disposed.
     */
    get isDisposed() {
        return this._isDisposed;
    }
    get plugin() {
        return this.registry.plugins[this.id];
    }
    /**
     * The plugin's schema.
     */
    get schema() {
        return this.plugin.schema;
    }
    /**
     * The plugin settings raw text value.
     */
    get raw() {
        return this.plugin.raw;
    }
    /**
     * Checks if any fields are different from the default value.
     */
    isDefault(user) {
        for (const key in this.schema.properties) {
            const value = user[key];
            const defaultValue = this.default(key);
            if (value === undefined ||
                defaultValue === undefined ||
                _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual(value, _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.emptyObject) ||
                _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual(value, _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.emptyArray)) {
                continue;
            }
            if (!_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual(value, defaultValue)) {
                return false;
            }
        }
        return true;
    }
    get isModified() {
        return !this.isDefault(this.user);
    }
    /**
     * The user settings.
     */
    get user() {
        return this.plugin.data.user;
    }
    /**
     * The published version of the NPM package containing these settings.
     */
    get version() {
        return this.plugin.version;
    }
    /**
     * Return the defaults in a commented JSON format.
     */
    annotatedDefaults() {
        return Private.annotatedDefaults(this.schema, this.id);
    }
    /**
     * Calculate the default value of a setting by iterating through the schema.
     *
     * @param key - The name of the setting whose default value is calculated.
     *
     * @returns A calculated default JSON value for a specific setting.
     */
    default(key) {
        return Private.reifyDefault(this.schema, key);
    }
    /**
     * Dispose of the plugin settings resources.
     */
    dispose() {
        if (this._isDisposed) {
            return;
        }
        this._isDisposed = true;
        _lumino_signaling__WEBPACK_IMPORTED_MODULE_3__.Signal.clearData(this);
    }
    /**
     * Get an individual setting.
     *
     * @param key - The name of the setting being retrieved.
     *
     * @returns The setting value.
     *
     * #### Notes
     * This method returns synchronously because it uses a cached copy of the
     * plugin settings that is synchronized with the registry.
     */
    get(key) {
        const { composite, user } = this;
        return {
            composite: composite[key] !== undefined ? copy(composite[key]) : undefined,
            user: user[key] !== undefined ? copy(user[key]) : undefined
        };
    }
    /**
     * Remove a single setting.
     *
     * @param key - The name of the setting being removed.
     *
     * @returns A promise that resolves when the setting is removed.
     *
     * #### Notes
     * This function is asynchronous because it writes to the setting registry.
     */
    remove(key) {
        return this.registry.remove(this.plugin.id, key);
    }
    /**
     * Save all of the plugin's user settings at once.
     */
    save(raw) {
        return this.registry.upload(this.plugin.id, raw);
    }
    /**
     * Set a single setting.
     *
     * @param key - The name of the setting being set.
     *
     * @param value - The value of the setting.
     *
     * @returns A promise that resolves when the setting has been saved.
     *
     * #### Notes
     * This function is asynchronous because it writes to the setting registry.
     */
    set(key, value) {
        return this.registry.set(this.plugin.id, key, value);
    }
    /**
     * Validates raw settings with comments.
     *
     * @param raw - The JSON with comments string being validated.
     *
     * @returns A list of errors or `null` if valid.
     */
    validate(raw) {
        const data = { composite: {}, user: {} };
        const { id, schema } = this.plugin;
        const validator = this.registry.validator;
        const version = this.version;
        return validator.validateData({ data, id, raw, schema, version }, false);
    }
    /**
     * Handle plugin changes in the setting registry.
     */
    _onPluginChanged(sender, plugin) {
        if (plugin === this.plugin.id) {
            this._changed.emit(undefined);
        }
    }
}
/**
 * A namespace for `SettingRegistry` statics.
 */
(function (SettingRegistry) {
    /**
     * Reconcile the menus.
     *
     * @param reference The reference list of menus.
     * @param addition The list of menus to add.
     * @param warn Warn if the command items are duplicated within the same menu.
     * @returns The reconciled list of menus.
     */
    function reconcileMenus(reference, addition, warn = false, addNewItems = true) {
        if (!reference) {
            return addition && addNewItems ? _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(addition) : [];
        }
        if (!addition) {
            return _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(reference);
        }
        const merged = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(reference);
        addition.forEach(menu => {
            const refIndex = merged.findIndex(ref => ref.id === menu.id);
            if (refIndex >= 0) {
                merged[refIndex] = Object.assign(Object.assign(Object.assign({}, merged[refIndex]), menu), { items: reconcileItems(merged[refIndex].items, menu.items, warn, addNewItems) });
            }
            else {
                if (addNewItems) {
                    merged.push(menu);
                }
            }
        });
        return merged;
    }
    SettingRegistry.reconcileMenus = reconcileMenus;
    /**
     * Merge two set of menu items.
     *
     * @param reference Reference set of menu items
     * @param addition New items to add
     * @param warn Whether to warn if item is duplicated; default to false
     * @returns The merged set of items
     */
    function reconcileItems(reference, addition, warn = false, addNewItems = true) {
        if (!reference) {
            return addition ? _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(addition) : undefined;
        }
        if (!addition) {
            return _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(reference);
        }
        const items = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(reference);
        // Merge array element depending on the type
        addition.forEach(item => {
            var _a;
            switch ((_a = item.type) !== null && _a !== void 0 ? _a : 'command') {
                case 'separator':
                    if (addNewItems) {
                        items.push(Object.assign({}, item));
                    }
                    break;
                case 'submenu':
                    if (item.submenu) {
                        const refIndex = items.findIndex(ref => { var _a, _b; return ref.type === 'submenu' && ((_a = ref.submenu) === null || _a === void 0 ? void 0 : _a.id) === ((_b = item.submenu) === null || _b === void 0 ? void 0 : _b.id); });
                        if (refIndex < 0) {
                            if (addNewItems) {
                                items.push(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(item));
                            }
                        }
                        else {
                            items[refIndex] = Object.assign(Object.assign(Object.assign({}, items[refIndex]), item), { submenu: reconcileMenus(items[refIndex].submenu
                                    ? [items[refIndex].submenu]
                                    : null, [item.submenu], warn, addNewItems)[0] });
                        }
                    }
                    break;
                case 'command':
                    if (item.command) {
                        const refIndex = items.findIndex(ref => {
                            var _a, _b;
                            return ref.command === item.command &&
                                ref.selector === item.selector &&
                                _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual((_a = ref.args) !== null && _a !== void 0 ? _a : {}, (_b = item.args) !== null && _b !== void 0 ? _b : {});
                        });
                        if (refIndex < 0) {
                            if (addNewItems) {
                                items.push(Object.assign({}, item));
                            }
                        }
                        else {
                            if (warn) {
                                console.warn(`Menu entry for command '${item.command}' is duplicated.`);
                            }
                            items[refIndex] = Object.assign(Object.assign({}, items[refIndex]), item);
                        }
                    }
            }
        });
        return items;
    }
    SettingRegistry.reconcileItems = reconcileItems;
    /**
     * Remove disabled entries from menu items
     *
     * @param items Menu items
     * @returns Filtered menu items
     */
    function filterDisabledItems(items) {
        return items.reduce((final, value) => {
            var _a;
            const copy = Object.assign({}, value);
            if (!copy.disabled) {
                if (copy.type === 'submenu') {
                    const { submenu } = copy;
                    if (submenu && !submenu.disabled) {
                        copy.submenu = Object.assign(Object.assign({}, submenu), { items: filterDisabledItems((_a = submenu.items) !== null && _a !== void 0 ? _a : []) });
                    }
                }
                final.push(copy);
            }
            return final;
        }, []);
    }
    SettingRegistry.filterDisabledItems = filterDisabledItems;
    /**
     * Reconcile default and user shortcuts and return the composite list.
     *
     * @param defaults - The list of default shortcuts.
     *
     * @param user - The list of user shortcut overrides and additions.
     *
     * @returns A loadable list of shortcuts (omitting disabled and overridden).
     */
    function reconcileShortcuts(defaults, user) {
        const memo = {};
        // If a user shortcut collides with another user shortcut warn and filter.
        user = user.filter(shortcut => {
            const keys = _lumino_commands__WEBPACK_IMPORTED_MODULE_0__.CommandRegistry.normalizeKeys(shortcut).join(RECORD_SEPARATOR);
            if (!keys) {
                console.warn('Skipping this shortcut because there are no actionable keys on this platform', shortcut);
                return false;
            }
            if (!(keys in memo)) {
                memo[keys] = {};
            }
            const { selector } = shortcut;
            if (!(selector in memo[keys])) {
                memo[keys][selector] = false; // Do not warn if a default shortcut conflicts.
                return true;
            }
            console.warn('Skipping this shortcut because it collides with another shortcut.', shortcut);
            return false;
        });
        // If a default shortcut collides with another default, warn and filter,
        // unless one of the shortcuts is a disabling shortcut (so look through
        // disabled shortcuts first). If a shortcut has already been added by the
        // user preferences, filter it out too (this includes shortcuts that are
        // disabled by user preferences).
        defaults = [
            ...defaults.filter(s => !!s.disabled),
            ...defaults.filter(s => !s.disabled)
        ].filter(shortcut => {
            const keys = _lumino_commands__WEBPACK_IMPORTED_MODULE_0__.CommandRegistry.normalizeKeys(shortcut).join(RECORD_SEPARATOR);
            if (!keys) {
                return false;
            }
            if (!(keys in memo)) {
                memo[keys] = {};
            }
            const { disabled, selector } = shortcut;
            if (!(selector in memo[keys])) {
                // Warn of future conflicts if the default shortcut is not disabled.
                memo[keys][selector] = !disabled;
                return true;
            }
            // We have a conflict now. Warn the user if we need to do so.
            if (memo[keys][selector]) {
                console.warn('Skipping this default shortcut because it collides with another default shortcut.', shortcut);
            }
            return false;
        });
        // Return all the shortcuts that should be registered
        return (user
            .concat(defaults)
            .filter(shortcut => !shortcut.disabled)
            // Fix shortcuts comparison in rjsf Form to avoid polluting the user settings
            .map(shortcut => {
            return Object.assign({ args: {} }, shortcut);
        }));
    }
    SettingRegistry.reconcileShortcuts = reconcileShortcuts;
    /**
     * Merge two set of toolbar items.
     *
     * @param reference Reference set of toolbar items
     * @param addition New items to add
     * @param warn Whether to warn if item is duplicated; default to false
     * @returns The merged set of items
     */
    function reconcileToolbarItems(reference, addition, warn = false) {
        if (!reference) {
            return addition ? _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(addition) : undefined;
        }
        if (!addition) {
            return _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(reference);
        }
        const items = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(reference);
        // Merge array element depending on the type
        addition.forEach(item => {
            // Name must be unique so it's sufficient to only compare it
            const refIndex = items.findIndex(ref => ref.name === item.name);
            if (refIndex < 0) {
                items.push(Object.assign({}, item));
            }
            else {
                if (warn &&
                    _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepEqual(Object.keys(item), Object.keys(items[refIndex]))) {
                    console.warn(`Toolbar item '${item.name}' is duplicated.`);
                }
                items[refIndex] = Object.assign(Object.assign({}, items[refIndex]), item);
            }
        });
        return items;
    }
    SettingRegistry.reconcileToolbarItems = reconcileToolbarItems;
})(SettingRegistry || (SettingRegistry = {}));
/**
 * A namespace for private module data.
 */
var Private;
(function (Private) {
    /**
     * The default indentation level, uses spaces instead of tabs.
     */
    const indent = '    ';
    /**
     * Replacement text for schema properties missing a `description` field.
     */
    const nondescript = '[missing schema description]';
    /**
     * Replacement text for schema properties missing a `title` field.
     */
    const untitled = '[missing schema title]';
    /**
     * Returns an annotated (JSON with comments) version of a schema's defaults.
     */
    function annotatedDefaults(schema, plugin) {
        const { description, properties, title } = schema;
        const keys = properties
            ? Object.keys(properties).sort((a, b) => a.localeCompare(b))
            : [];
        const length = Math.max((description || nondescript).length, plugin.length);
        return [
            '{',
            prefix(`${title || untitled}`),
            prefix(plugin),
            prefix(description || nondescript),
            prefix('*'.repeat(length)),
            '',
            join(keys.map(key => defaultDocumentedValue(schema, key))),
            '}'
        ].join('\n');
    }
    Private.annotatedDefaults = annotatedDefaults;
    /**
     * Returns an annotated (JSON with comments) version of a plugin's
     * setting data.
     */
    function annotatedPlugin(plugin, data) {
        const { description, title } = plugin.schema;
        const keys = Object.keys(data).sort((a, b) => a.localeCompare(b));
        const length = Math.max((description || nondescript).length, plugin.id.length);
        return [
            '{',
            prefix(`${title || untitled}`),
            prefix(plugin.id),
            prefix(description || nondescript),
            prefix('*'.repeat(length)),
            '',
            join(keys.map(key => documentedValue(plugin.schema, key, data[key]))),
            '}'
        ].join('\n');
    }
    Private.annotatedPlugin = annotatedPlugin;
    /**
     * Returns the default value-with-documentation-string for a
     * specific schema property.
     */
    function defaultDocumentedValue(schema, key) {
        const props = (schema.properties && schema.properties[key]) || {};
        const type = props['type'];
        const description = props['description'] || nondescript;
        const title = props['title'] || '';
        const reified = reifyDefault(schema, key);
        const spaces = indent.length;
        const defaults = reified !== undefined
            ? prefix(`"${key}": ${JSON.stringify(reified, null, spaces)}`, indent)
            : prefix(`"${key}": ${type}`);
        return [prefix(title), prefix(description), defaults]
            .filter(str => str.length)
            .join('\n');
    }
    /**
     * Returns a value-with-documentation-string for a specific schema property.
     */
    function documentedValue(schema, key, value) {
        const props = schema.properties && schema.properties[key];
        const description = (props && props['description']) || nondescript;
        const title = (props && props['title']) || untitled;
        const spaces = indent.length;
        const attribute = prefix(`"${key}": ${JSON.stringify(value, null, spaces)}`, indent);
        return [prefix(title), prefix(description), attribute].join('\n');
    }
    /**
     * Returns a joined string with line breaks and commas where appropriate.
     */
    function join(body) {
        return body.reduce((acc, val, idx) => {
            const rows = val.split('\n');
            const last = rows[rows.length - 1];
            const comment = last.trim().indexOf('//') === 0;
            const comma = comment || idx === body.length - 1 ? '' : ',';
            const separator = idx === body.length - 1 ? '' : '\n\n';
            return acc + val + comma + separator;
        }, '');
    }
    /**
     * Returns a documentation string with a comment prefix added on every line.
     */
    function prefix(source, pre = `${indent}// `) {
        return pre + source.split('\n').join(`\n${pre}`);
    }
    /**
     * Create a fully extrapolated default value for a root key in a schema.
     */
    function reifyDefault(schema, root) {
        var _a, _b, _c;
        const definitions = schema.definitions;
        // If the property is at the root level, traverse its schema.
        schema = (root ? (_a = schema.properties) === null || _a === void 0 ? void 0 : _a[root] : schema) || {};
        if (schema.type === 'object') {
            // Make a copy of the default value to populate.
            const result = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(schema.default);
            // Iterate through and populate each child property.
            const props = schema.properties || {};
            for (const property in props) {
                result[property] = reifyDefault(props[property]);
            }
            return result;
        }
        else if (schema.type === 'array') {
            // Make a copy of the default value to populate.
            const result = _lumino_coreutils__WEBPACK_IMPORTED_MODULE_1__.JSONExt.deepCopy(schema.default);
            // Items defines the properties of each item in the array
            let props = schema.items || {};
            // Use referenced definition if one exists
            if (props['$ref'] && definitions) {
                const ref = props['$ref'].replace('#/definitions/', '');
                props = (_b = definitions[ref]) !== null && _b !== void 0 ? _b : {};
            }
            // Iterate through the items in the array and fill in defaults
            for (const item in result) {
                // Use the values that are hard-coded in the default array over the defaults for each field.
                const reified = reifyDefault(props) || {};
                for (const prop in reified) {
                    if ((_c = result[item]) === null || _c === void 0 ? void 0 : _c[prop]) {
                        reified[prop] = result[item][prop];
                    }
                }
                result[item] = reified;
            }
            return result;
        }
        else {
            return schema.default;
        }
    }
    Private.reifyDefault = reifyDefault;
})(Private || (Private = {}));


/***/ }),

/***/ "../../packages/settingregistry/lib/tokens.js":
/*!****************************************************!*\
  !*** ../../packages/settingregistry/lib/tokens.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ISettingRegistry": () => (/* binding */ ISettingRegistry)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* -----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * The setting registry token.
 */
const ISettingRegistry = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/coreutils:ISettingRegistry');


/***/ }),

/***/ "../../packages/settingregistry/lib/plugin-schema.json":
/*!*************************************************************!*\
  !*** ../../packages/settingregistry/lib/plugin-schema.json ***!
  \*************************************************************/
/***/ ((module) => {

module.exports = JSON.parse('{"$schema":"http://json-schema.org/draft-07/schema","title":"JupyterLab Plugin Settings/Preferences Schema","description":"JupyterLab plugin settings/preferences schema","version":"1.0.0","type":"object","additionalProperties":true,"properties":{"jupyter.lab.internationalization":{"type":"object","properties":{"selectors":{"type":"array","items":{"type":"string","minLength":1}},"domain":{"type":"string","minLength":1}}},"jupyter.lab.menus":{"type":"object","properties":{"main":{"title":"Main menu entries","description":"List of menu items to add to the main menubar.","items":{"$ref":"#/definitions/menu"},"type":"array","default":[]},"context":{"title":"The application context menu.","description":"List of context menu items.","items":{"allOf":[{"$ref":"#/definitions/menuItem"},{"properties":{"selector":{"description":"The CSS selector for the context menu item.","type":"string"}}}]},"type":"array","default":[]}},"additionalProperties":false},"jupyter.lab.setting-deprecated":{"type":"boolean","default":false},"jupyter.lab.setting-icon":{"type":"string","default":""},"jupyter.lab.setting-icon-class":{"type":"string","default":""},"jupyter.lab.setting-icon-label":{"type":"string","default":"Plugin"},"jupyter.lab.shortcuts":{"items":{"$ref":"#/definitions/shortcut"},"type":"array","default":[]},"jupyter.lab.toolbars":{"properties":{"^\\\\w[\\\\w-\\\\.]*$":{"items":{"$ref":"#/definitions/toolbarItem"},"type":"array","default":[]}},"type":"object","default":{}},"jupyter.lab.transform":{"type":"boolean","default":false}},"definitions":{"menu":{"properties":{"disabled":{"description":"Whether the menu is disabled or not","type":"boolean","default":false},"icon":{"description":"Menu icon id","type":"string"},"id":{"description":"Menu unique id","oneOf":[{"type":"string","enum":["jp-menu-file","jp-menu-file-new","jp-menu-edit","jp-menu-help","jp-menu-kernel","jp-menu-run","jp-menu-settings","jp-menu-view","jp-menu-tabs"]},{"type":"string","pattern":"[a-z][a-z0-9\\\\-_]+"}]},"items":{"description":"Menu items","type":"array","items":{"$ref":"#/definitions/menuItem"}},"label":{"description":"Menu label","type":"string"},"mnemonic":{"description":"Mnemonic index for the label","type":"number","minimum":-1,"default":-1},"rank":{"description":"Menu rank","type":"number","minimum":0}},"required":["id"],"type":"object"},"menuItem":{"properties":{"args":{"description":"Command arguments","type":"object"},"command":{"description":"Command id","type":"string"},"disabled":{"description":"Whether the item is disabled or not","type":"boolean","default":false},"type":{"description":"Item type","type":"string","enum":["command","submenu","separator"],"default":"command"},"rank":{"description":"Item rank","type":"number","minimum":0},"submenu":{"oneOf":[{"$ref":"#/definitions/menu"},{"type":"null"}]}},"type":"object"},"shortcut":{"properties":{"args":{"title":"The arguments for the command","type":"object"},"command":{"title":"The command id","description":"The command executed when the binding is matched.","type":"string"},"disabled":{"description":"Whether this shortcut is disabled or not.","type":"boolean","default":false},"keys":{"title":"The key sequence for the binding","description":"The key shortcut like `Accel A` or the sequence of shortcuts to press like [`Accel A`, `B`]","items":{"type":"string"},"type":"array"},"macKeys":{"title":"The key sequence for the binding on macOS","description":"The key shortcut like `Cmd A` or the sequence of shortcuts to press like [`Cmd A`, `B`]","items":{"type":"string"},"type":"array"},"winKeys":{"title":"The key sequence for the binding on Windows","description":"The key shortcut like `Ctrl A` or the sequence of shortcuts to press like [`Ctrl A`, `B`]","items":{"type":"string"},"type":"array"},"linuxKeys":{"title":"The key sequence for the binding on Linux","description":"The key shortcut like `Ctrl A` or the sequence of shortcuts to press like [`Ctrl A`, `B`]","items":{"type":"string"},"type":"array"},"selector":{"title":"CSS selector","type":"string"}},"required":["command","keys","selector"],"type":"object"},"toolbarItem":{"properties":{"name":{"title":"Unique name","type":"string"},"args":{"title":"Command arguments","type":"object"},"command":{"title":"Command id","type":"string","default":""},"disabled":{"title":"Whether the item is ignored or not","type":"boolean","default":false},"icon":{"title":"Item icon id","description":"If defined, it will override the command icon","type":"string"},"label":{"title":"Item label","description":"If defined, it will override the command label","type":"string"},"type":{"title":"Item type","type":"string","enum":["command","spacer"]},"rank":{"title":"Item rank","type":"number","minimum":0,"default":50}},"required":["name"],"additionalProperties":false,"type":"object"}}}');

/***/ })

}]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicGFja2FnZXNfc2V0dGluZ3JlZ2lzdHJ5X2xpYl9pbmRleF9qcy5iM2RiZTdiNGZhNDI4YTZkYjQwOC5qcyIsIm1hcHBpbmdzIjoiOzs7Ozs7Ozs7Ozs7Ozs7Ozs7QUFBQTs7OytFQUcrRTtBQUMvRTs7O0dBR0c7QUFFK0I7QUFDVDs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDVnpCLDBDQUEwQztBQUMxQywyREFBMkQ7QUFHUjtBQVd4QjtBQUMwQztBQUNqQjtBQUM5QjtBQUNTO0FBQ1c7QUFHMUM7O0dBRUc7QUFDSCxNQUFNLElBQUksR0FBRywrREFBZ0IsQ0FBQztBQUU5Qjs7OztHQUlHO0FBQ0gsTUFBTSx5QkFBeUIsR0FBRyxJQUFJLENBQUM7QUFFdkM7O0dBRUc7QUFDSCxNQUFNLGdCQUFnQixHQUFHLE1BQU0sQ0FBQyxZQUFZLENBQUMsRUFBRSxDQUFDLENBQUM7QUEyRGpEOztHQUVHO0FBQ0ksTUFBTSxzQkFBc0I7SUFDakM7O09BRUc7SUFDSDtRQWlJUSxjQUFTLEdBQUcsSUFBSSw0Q0FBRyxDQUFDLEVBQUUsV0FBVyxFQUFFLElBQUksRUFBRSxDQUFDLENBQUM7UUFDM0MsZUFBVSxHQUFHLElBQUksNENBQUcsRUFBRSxDQUFDO1FBakk3QixJQUFJLENBQUMsU0FBUyxDQUFDLFNBQVMsQ0FBQyxnREFBTSxFQUFFLDBCQUEwQixDQUFDLENBQUM7UUFDN0QsSUFBSSxDQUFDLFVBQVUsQ0FBQyxTQUFTLENBQUMsZ0RBQU0sRUFBRSwwQkFBMEIsQ0FBQyxDQUFDO0lBQ2hFLENBQUM7SUFFRDs7Ozs7Ozs7Ozs7T0FXRztJQUNILFlBQVksQ0FDVixNQUFnQyxFQUNoQyxRQUFRLEdBQUcsSUFBSTtRQUVmLE1BQU0sUUFBUSxHQUFHLElBQUksQ0FBQyxVQUFVLENBQUMsU0FBUyxDQUFDLE1BQU0sQ0FBQyxFQUFFLENBQUMsQ0FBQztRQUN0RCxNQUFNLE9BQU8sR0FBRyxJQUFJLENBQUMsU0FBUyxDQUFDLFNBQVMsQ0FBQyxNQUFNLENBQUMsRUFBRSxD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SyxDQUN2Qyx3Q0FBd0MsQ0FDekMsQ0FBQyIsInNvdXJjZXMiOlsid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zZXR0aW5ncmVnaXN0cnkvc3JjL2luZGV4LnRzIiwid2VicGFjazovL0BqdXB5dGVybGFiL2FwcGxpY2F0aW9uLXRvcC8uLi8uLi9wYWNrYWdlcy9zZXR0aW5ncmVnaXN0cnkvc3JjL3NldHRpbmdyZWdpc3RyeS50cyIsIndlYnBhY2s6Ly9AanVweXRlcmxhYi9hcHBsaWNhdGlvbi10b3AvLi4vLi4vcGFja2FnZXMvc2V0dGluZ3JlZ2lzdHJ5L3NyYy90b2tlbnMudHMiXSwic291cmNlc0NvbnRlbnQiOlsiLyogLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnwgQ29weXJpZ2h0IChjKSBKdXB5dGVyIERldmVsb3BtZW50IFRlYW0uXG58IERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG58LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSovXG4vKipcbiAqIEBwYWNrYWdlRG9jdW1lbnRhdGlvblxuICogQG1vZHVsZSBzZXR0aW5ncmVnaXN0cnlcbiAqL1xuXG5leHBvcnQgKiBmcm9tICcuL3NldHRpbmdyZWdpc3RyeSc7XG5leHBvcnQgKiBmcm9tICcuL3Rva2Vucyc7XG4iLCIvLyBDb3B5cmlnaHQgKGMpIEp1cHl0ZXIgRGV2ZWxvcG1lbnQgVGVhbS5cbi8vIERpc3RyaWJ1dGVkIHVuZGVyIHRoZSB0ZXJtcyBvZiB0aGUgTW9kaWZpZWQgQlNEIExpY2Vuc2UuXG5cbmltcG9ydCB7IElEYXRhQ29ubmVjdG9yIH0gZnJvbSAnQGp1cHl0ZXJsYWIvc3RhdGVkYic7XG5pbXBvcnQgeyBDb21tYW5kUmVnaXN0cnkgfSBmcm9tICdAbHVtaW5vL2NvbW1hbmRzJztcbmltcG9ydCB7XG4gIEpTT05FeHQsXG4gIEpTT05PYmplY3QsXG4gIEpTT05WYWx1ZSxcbiAgUGFydGlhbEpTT05BcnJheSxcbiAgUGFydGlhbEpTT05PYmplY3QsXG4gIFBhcnRpYWxKU09OVmFsdWUsXG4gIFJlYWRvbmx5SlNPTk9iamVjdCxcbiAgUmVhZG9ubHlQYXJ0aWFsSlNPTk9iamVjdCxcbiAgUmVhZG9ubHlQYXJ0aWFsSlNPTlZhbHVlXG59IGZyb20gJ0BsdW1pbm8vY29yZXV0aWxzJztcbmltcG9ydCB7IERpc3Bvc2FibGVEZWxlZ2F0ZSwgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgSVNpZ25hbCwgU2lnbmFsIH0gZnJvbSAnQGx1bWluby9zaWduYWxpbmcnO1xuaW1wb3J0IEFqdiBmcm9tICdhanYnO1xuaW1wb3J0ICogYXMganNvbjUgZnJvbSAnanNvbjUnO1xuaW1wb3J0IFNDSEVNQSBmcm9tICcuL3BsdWdpbi1zY2hlbWEuanNvbic7XG5pbXBvcnQgeyBJU2V0dGluZ1JlZ2lzdHJ5IH0gZnJvbSAnLi90b2tlbnMnO1xuXG4vKipcbiAqIEFuIGFsaWFzIGZvciB0aGUgSlNPTiBkZWVwIGNvcHkgZnVuY3Rpb24uXG4gKi9cbmNvbnN0IGNvcHkgPSBKU09ORXh0LmRlZXBDb3B5O1xuXG4vKipcbiAqIFRoZSBkZWZhdWx0IG51bWJlciBvZiBtaWxsaXNlY29uZHMgYmVmb3JlIGEgYGxvYWQoKWAgY2FsbCB0byB0aGUgcmVnaXN0cnlcbiAqIHdpbGwgd2FpdCBiZWZvcmUgdGltaW5nIG91dCBpZiBpdCByZXF1aXJlcyBhIHRyYW5zZm9ybWF0aW9uIHRoYXQgaGFzIG5vdCBiZWVuXG4gKiByZWdpc3RlcmVkLlxuICovXG5jb25zdCBERUZBVUxUX1RSQU5TRk9STV9USU1FT1VUID0gMTAwMDtcblxuLyoqXG4gKiBUaGUgQVNDSUkgcmVjb3JkIHNlcGFyYXRvciBjaGFyYWN0ZXIuXG4gKi9cbmNvbnN0IFJFQ09SRF9TRVBBUkFUT1IgPSBTdHJpbmcuZnJvbUNoYXJDb2RlKDMwKTtcblxuLyoqXG4gKiBBbiBpbXBsZW1lbnRhdGlvbiBvZiBhIHNjaGVtYSB2YWxpZGF0b3IuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVNjaGVtYVZhbGlkYXRvciB7XG4gIC8qKlxuICAgKiBWYWxpZGF0ZSBhIHBsdWdpbidzIHNjaGVtYSBhbmQgdXNlciBkYXRhOyBwb3B1bGF0ZSB0aGUgYGNvbXBvc2l0ZWAgZGF0YS5cbiAgICpcbiAgICogQHBhcmFtIHBsdWdpbiAtIFRoZSBwbHVnaW4gYmVpbmcgdmFsaWRhdGVkLiBJdHMgYGNvbXBvc2l0ZWAgZGF0YSB3aWxsIGJlXG4gICAqIHBvcHVsYXRlZCBieSByZWZlcmVuY2UuXG4gICAqXG4gICAqIEBwYXJhbSBwb3B1bGF0ZSAtIFdoZXRoZXIgcGx1Z2luIGRhdGEgc2hvdWxkIGJlIHBvcHVsYXRlZCwgZGVmYXVsdHMgdG9cbiAgICogYHRydWVgLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIGxpc3Qgb2YgZXJyb3JzIGlmIGVpdGhlciB0aGUgc2NoZW1hIG9yIGRhdGEgZmFpbCB0byB2YWxpZGF0ZSBvclxuICAgKiBgbnVsbGAgaWYgdGhlcmUgYXJlIG5vIGVycm9ycy5cbiAgICovXG4gIHZhbGlkYXRlRGF0YShcbiAgICBwbHVnaW46IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbixcbiAgICBwb3B1bGF0ZT86IGJvb2xlYW5cbiAgKTogSVNjaGVtYVZhbGlkYXRvci5JRXJyb3JbXSB8IG51bGw7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIHNjaGVtYSB2YWxpZGF0b3IgaW50ZXJmYWNlcy5cbiAqL1xuZXhwb3J0IG5hbWVzcGFjZSBJU2NoZW1hVmFsaWRhdG9yIHtcbiAgLyoqXG4gICAqIEEgc2NoZW1hIHZhbGlkYXRpb24gZXJyb3IgZGVmaW5pdGlvbi5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSUVycm9yIHtcbiAgICAvKipcbiAgICAgKiBUaGUgcGF0aCBpbiB0aGUgZGF0YSB3aGVyZSB0aGUgZXJyb3Igb2NjdXJyZWQuXG4gICAgICovXG4gICAgZGF0YVBhdGg6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBrZXl3b3JkIHdob3NlIHZhbGlkYXRpb24gZmFpbGVkLlxuICAgICAqL1xuICAgIGtleXdvcmQ6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBlcnJvciBtZXNzYWdlLlxuICAgICAqL1xuICAgIG1lc3NhZ2U6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIE9wdGlvbmFsIHBhcmFtZXRlciBtZXRhZGF0YSB0aGF0IG1pZ2h0IGJlIGluY2x1ZGVkIGluIGFuIGVycm9yLlxuICAgICAqL1xuICAgIHBhcmFtcz86IFJlYWRvbmx5SlNPTk9iamVjdDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwYXRoIGluIHRoZSBzY2hlbWEgd2hlcmUgdGhlIGVycm9yIG9jY3VycmVkLlxuICAgICAqL1xuICAgIHNjaGVtYVBhdGg6IHN0cmluZztcbiAgfVxufVxuXG4vKipcbiAqIFRoZSBkZWZhdWx0IGltcGxlbWVudGF0aW9uIG9mIGEgc2NoZW1hIHZhbGlkYXRvci5cbiAqL1xuZXhwb3J0IGNsYXNzIERlZmF1bHRTY2hlbWFWYWxpZGF0b3IgaW1wbGVtZW50cyBJU2NoZW1hVmFsaWRhdG9yIHtcbiAgLyoqXG4gICAqIEluc3RhbnRpYXRlIGEgc2NoZW1hIHZhbGlkYXRvci5cbiAgICovXG4gIGNvbnN0cnVjdG9yKCkge1xuICAgIHRoaXMuX2NvbXBvc2VyLmFkZFNjaGVtYShTQ0hFTUEsICdqdXB5dGVybGFiLXBsdWdpbi1zY2hlbWEnKTtcbiAgICB0aGlzLl92YWxpZGF0b3IuYWRkU2NoZW1hKFNDSEVNQSwgJ2p1cHl0ZXJsYWItcGx1Z2luLXNjaGVtYScpO1xuICB9XG5cbiAgLyoqXG4gICAqIFZhbGlkYXRlIGEgcGx1Z2luJ3Mgc2NoZW1hIGFuZCB1c2VyIGRhdGE7IHBvcHVsYXRlIHRoZSBgY29tcG9zaXRlYCBkYXRhLlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIHBsdWdpbiBiZWluZyB2YWxpZGF0ZWQuIEl0cyBgY29tcG9zaXRlYCBkYXRhIHdpbGwgYmVcbiAgICogcG9wdWxhdGVkIGJ5IHJlZmVyZW5jZS5cbiAgICpcbiAgICogQHBhcmFtIHBvcHVsYXRlIC0gV2hldGhlciBwbHVnaW4gZGF0YSBzaG91bGQgYmUgcG9wdWxhdGVkLCBkZWZhdWx0cyB0b1xuICAgKiBgdHJ1ZWAuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgbGlzdCBvZiBlcnJvcnMgaWYgZWl0aGVyIHRoZSBzY2hlbWEgb3IgZGF0YSBmYWlsIHRvIHZhbGlkYXRlIG9yXG4gICAqIGBudWxsYCBpZiB0aGVyZSBhcmUgbm8gZXJyb3JzLlxuICAgKi9cbiAgdmFsaWRhdGVEYXRhKFxuICAgIHBsdWdpbjogSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luLFxuICAgIHBvcHVsYXRlID0gdHJ1ZVxuICApOiBJU2NoZW1hVmFsaWRhdG9yLklFcnJvcltdIHwgbnVsbCB7XG4gICAgY29uc3QgdmFsaWRhdGUgPSB0aGlzLl92YWxpZGF0b3IuZ2V0U2NoZW1hKHBsdWdpbi5pZCk7XG4gICAgY29uc3QgY29tcG9zZSA9IHRoaXMuX2NvbXBvc2VyLmdldFNjaGVtYShwbHVnaW4uaWQpO1xuXG4gICAgLy8gSWYgdGhlIHNjaGVtYXMgZG8gbm90IGV4aXN0LCBhZGQgdGhlbSB0byB0aGUgdmFsaWRhdG9yIGFuZCBjb250aW51ZS5cbiAgICBpZiAoIXZhbGlkYXRlIHx8ICFjb21wb3NlKSB7XG4gICAgICBpZiAocGx1Z2luLnNjaGVtYS50eXBlICE9PSAnb2JqZWN0Jykge1xuICAgICAgICBjb25zdCBrZXl3b3JkID0gJ3NjaGVtYSc7XG4gICAgICAgIGNvbnN0IG1lc3NhZ2UgPVxuICAgICAgICAgIGBTZXR0aW5nIHJlZ2lzdHJ5IHNjaGVtYXMnIHJvb3QtbGV2ZWwgdHlwZSBtdXN0IGJlIGAgK1xuICAgICAgICAgIGAnb2JqZWN0JywgcmVqZWN0aW5nIHR5cGU6ICR7cGx1Z2luLnNjaGVtYS50eXBlfWA7XG5cbiAgICAgICAgcmV0dXJuIFt7IGRhdGFQYXRoOiAndHlwZScsIGtleXdvcmQsIHNjaGVtYVBhdGg6ICcnLCBtZXNzYWdlIH1dO1xuICAgICAgfVxuXG4gICAgICBjb25zdCBlcnJvcnMgPSB0aGlzLl9hZGRTY2hlbWEocGx1Z2luLmlkLCBwbHVnaW4uc2NoZW1hKTtcblxuICAgICAgcmV0dXJuIGVycm9ycyB8fCB0aGlzLnZhbGlkYXRlRGF0YShwbHVnaW4pO1xuICAgIH1cblxuICAgIC8vIFBhcnNlIHRoZSByYXcgY29tbWVudGVkIEpTT04gaW50byBhIHVzZXIgbWFwLlxuICAgIGxldCB1c2VyOiBKU09OT2JqZWN0O1xuICAgIHRyeSB7XG4gICAgICB1c2VyID0ganNvbjUucGFyc2UocGx1Z2luLnJhdykgYXMgSlNPTk9iamVjdDtcbiAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgaWYgKGVycm9yIGluc3RhbmNlb2YgU3ludGF4RXJyb3IpIHtcbiAgICAgICAgcmV0dXJuIFtcbiAgICAgICAgICB7XG4gICAgICAgICAgICBkYXRhUGF0aDogJycsXG4gICAgICAgICAgICBrZXl3b3JkOiAnc3ludGF4JyxcbiAgICAgICAgICAgIHNjaGVtYVBhdGg6ICcnLFxuICAgICAgICAgICAgbWVzc2FnZTogZXJyb3IubWVzc2FnZVxuICAgICAgICAgIH1cbiAgICAgICAgXTtcbiAgICAgIH1cblxuICAgICAgY29uc3QgeyBjb2x1bW4sIGRlc2NyaXB0aW9uIH0gPSBlcnJvcjtcbiAgICAgIGNvbnN0IGxpbmUgPSBlcnJvci5saW5lTnVtYmVyO1xuXG4gICAgICByZXR1cm4gW1xuICAgICAgICB7XG4gICAgICAgICAgZGF0YVBhdGg6ICcnLFxuICAgICAgICAgIGtleXdvcmQ6ICdwYXJzZScsXG4gICAgICAgICAgc2NoZW1hUGF0aDogJycsXG4gICAgICAgICAgbWVzc2FnZTogYCR7ZGVzY3JpcHRpb259IChsaW5lICR7bGluZX0gY29sdW1uICR7Y29sdW1ufSlgXG4gICAgICAgIH1cbiAgICAgIF07XG4gICAgfVxuXG4gICAgaWYgKCF2YWxpZGF0ZSh1c2VyKSkge1xuICAgICAgcmV0dXJuIHZhbGlkYXRlLmVycm9ycyBhcyBJU2NoZW1hVmFsaWRhdG9yLklFcnJvcltdO1xuICAgIH1cblxuICAgIC8vIENvcHkgdGhlIHVzZXIgZGF0YSBiZWZvcmUgbWVyZ2luZyBkZWZhdWx0cyBpbnRvIGNvbXBvc2l0ZSBtYXAuXG4gICAgY29uc3QgY29tcG9zaXRlID0gY29weSh1c2VyKTtcblxuICAgIGlmICghY29tcG9zZShjb21wb3NpdGUpKSB7XG4gICAgICByZXR1cm4gY29tcG9zZS5lcnJvcnMgYXMgSVNjaGVtYVZhbGlkYXRvci5JRXJyb3JbXTtcbiAgICB9XG5cbiAgICBpZiAocG9wdWxhdGUpIHtcbiAgICAgIHBsdWdpbi5kYXRhID0geyBjb21wb3NpdGUsIHVzZXIgfTtcbiAgICB9XG5cbiAgICByZXR1cm4gbnVsbDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGQgYSBzY2hlbWEgdG8gdGhlIHZhbGlkYXRvci5cbiAgICpcbiAgICogQHBhcmFtIHBsdWdpbiAtIFRoZSBwbHVnaW4gSUQuXG4gICAqXG4gICAqIEBwYXJhbSBzY2hlbWEgLSBUaGUgc2NoZW1hIGJlaW5nIGFkZGVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIGxpc3Qgb2YgZXJyb3JzIGlmIHRoZSBzY2hlbWEgZmFpbHMgdG8gdmFsaWRhdGUgb3IgYG51bGxgIGlmIHRoZXJlXG4gICAqIGFyZSBubyBlcnJvcnMuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogSXQgaXMgc2FmZSB0byBjYWxsIHRoaXMgZnVuY3Rpb24gbXVsdGlwbGUgdGltZXMgd2l0aCB0aGUgc2FtZSBwbHVnaW4gbmFtZS5cbiAgICovXG4gIHByaXZhdGUgX2FkZFNjaGVtYShcbiAgICBwbHVnaW46IHN0cmluZyxcbiAgICBzY2hlbWE6IElTZXR0aW5nUmVnaXN0cnkuSVNjaGVtYVxuICApOiBJU2NoZW1hVmFsaWRhdG9yLklFcnJvcltdIHwgbnVsbCB7XG4gICAgY29uc3QgY29tcG9zZXIgPSB0aGlzLl9jb21wb3NlcjtcbiAgICBjb25zdCB2YWxpZGF0b3IgPSB0aGlzLl92YWxpZGF0b3I7XG4gICAgY29uc3QgdmFsaWRhdGUgPSB2YWxpZGF0b3IuZ2V0U2NoZW1hKCdqdXB5dGVybGFiLXBsdWdpbi1zY2hlbWEnKSE7XG5cbiAgICAvLyBWYWxpZGF0ZSBhZ2FpbnN0IHRoZSBtYWluIHNjaGVtYS5cbiAgICBpZiAoISh2YWxpZGF0ZSEoc2NoZW1hKSBhcyBib29sZWFuKSkge1xuICAgICAgcmV0dXJuIHZhbGlkYXRlIS5lcnJvcnMgYXMgSVNjaGVtYVZhbGlkYXRvci5JRXJyb3JbXTtcbiAgICB9XG5cbiAgICAvLyBWYWxpZGF0ZSBhZ2FpbnN0IHRoZSBKU09OIHNjaGVtYSBtZXRhLXNjaGVtYS5cbiAgICBpZiAoISh2YWxpZGF0b3IudmFsaWRhdGVTY2hlbWEoc2NoZW1hKSBhcyBib29sZWFuKSkge1xuICAgICAgcmV0dXJuIHZhbGlkYXRvci5lcnJvcnMgYXMgSVNjaGVtYVZhbGlkYXRvci5JRXJyb3JbXTtcbiAgICB9XG5cbiAgICAvLyBSZW1vdmUgaWYgc2NoZW1hIGFscmVhZHkgZXhpc3RzLlxuICAgIGNvbXBvc2VyLnJlbW92ZVNjaGVtYShwbHVnaW4pO1xuICAgIHZhbGlkYXRvci5yZW1vdmVTY2hlbWEocGx1Z2luKTtcblxuICAgIC8vIEFkZCBzY2hlbWEgdG8gdGhlIHZhbGlkYXRvciBhbmQgY29tcG9zZXIuXG4gICAgY29tcG9zZXIuYWRkU2NoZW1hKHNjaGVtYSwgcGx1Z2luKTtcbiAgICB2YWxpZGF0b3IuYWRkU2NoZW1hKHNjaGVtYSwgcGx1Z2luKTtcblxuICAgIHJldHVybiBudWxsO1xuICB9XG5cbiAgcHJpdmF0ZSBfY29tcG9zZXIgPSBuZXcgQWp2KHsgdXNlRGVmYXVsdHM6IHRydWUgfSk7XG4gIHByaXZhdGUgX3ZhbGlkYXRvciA9IG5ldyBBanYoKTtcbn1cblxuLyoqXG4gKiBUaGUgZGVmYXVsdCBjb25jcmV0ZSBpbXBsZW1lbnRhdGlvbiBvZiBhIHNldHRpbmcgcmVnaXN0cnkuXG4gKi9cbmV4cG9ydCBjbGFzcyBTZXR0aW5nUmVnaXN0cnkgaW1wbGVtZW50cyBJU2V0dGluZ1JlZ2lzdHJ5IHtcbiAgLyoqXG4gICAqIENyZWF0ZSBhIG5ldyBzZXR0aW5nIHJlZ2lzdHJ5LlxuICAgKi9cbiAgY29uc3RydWN0b3Iob3B0aW9uczogU2V0dGluZ1JlZ2lzdHJ5LklPcHRpb25zKSB7XG4gICAgdGhpcy5jb25uZWN0b3IgPSBvcHRpb25zLmNvbm5lY3RvcjtcbiAgICB0aGlzLnZhbGlkYXRvciA9IG9wdGlvbnMudmFsaWRhdG9yIHx8IG5ldyBEZWZhdWx0U2NoZW1hVmFsaWRhdG9yKCk7XG4gICAgdGhpcy5fdGltZW91dCA9IG9wdGlvbnMudGltZW91dCB8fCBERUZBVUxUX1RSQU5TRk9STV9USU1FT1VUO1xuXG4gICAgLy8gUHJlbG9hZCB3aXRoIGFueSBhdmFpbGFibGUgZGF0YSBhdCBpbnN0YW50aWF0aW9uLXRpbWUuXG4gICAgaWYgKG9wdGlvbnMucGx1Z2lucykge1xuICAgICAgdGhpcy5fcmVhZHkgPSB0aGlzLl9wcmVsb2FkKG9wdGlvbnMucGx1Z2lucyk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBkYXRhIGNvbm5lY3RvciB1c2VkIGJ5IHRoZSBzZXR0aW5nIHJlZ2lzdHJ5LlxuICAgKi9cbiAgcmVhZG9ubHkgY29ubmVjdG9yOiBJRGF0YUNvbm5lY3RvcjxJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW4sIHN0cmluZywgc3RyaW5nPjtcblxuICAvKipcbiAgICogVGhlIHNjaGVtYSBvZiB0aGUgc2V0dGluZyByZWdpc3RyeS5cbiAgICovXG4gIHJlYWRvbmx5IHNjaGVtYSA9IFNDSEVNQSBhcyBJU2V0dGluZ1JlZ2lzdHJ5LklTY2hlbWE7XG5cbiAgLyoqXG4gICAqIFRoZSBzY2hlbWEgdmFsaWRhdG9yIHVzZWQgYnkgdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAqL1xuICByZWFkb25seSB2YWxpZGF0b3I6IElTY2hlbWFWYWxpZGF0b3I7XG5cbiAgLyoqXG4gICAqIEEgc2lnbmFsIHRoYXQgZW1pdHMgdGhlIG5hbWUgb2YgYSBwbHVnaW4gd2hlbiBpdHMgc2V0dGluZ3MgY2hhbmdlLlxuICAgKi9cbiAgZ2V0IHBsdWdpbkNoYW5nZWQoKTogSVNpZ25hbDx0aGlzLCBzdHJpbmc+IHtcbiAgICByZXR1cm4gdGhpcy5fcGx1Z2luQ2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY29sbGVjdGlvbiBvZiBzZXR0aW5nIHJlZ2lzdHJ5IHBsdWdpbnMuXG4gICAqL1xuICByZWFkb25seSBwbHVnaW5zOiB7XG4gICAgW25hbWU6IHN0cmluZ106IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbjtcbiAgfSA9IE9iamVjdC5jcmVhdGUobnVsbCk7XG5cbiAgLyoqXG4gICAqIEdldCBhbiBpbmRpdmlkdWFsIHNldHRpbmcuXG4gICAqXG4gICAqIEBwYXJhbSBwbHVnaW4gLSBUaGUgbmFtZSBvZiB0aGUgcGx1Z2luIHdob3NlIHNldHRpbmdzIGFyZSBiZWluZyByZXRyaWV2ZWQuXG4gICAqXG4gICAqIEBwYXJhbSBrZXkgLSBUaGUgbmFtZSBvZiB0aGUgc2V0dGluZyBiZWluZyByZXRyaWV2ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIHNldHRpbmcgaXMgcmV0cmlldmVkLlxuICAgKi9cbiAgYXN5bmMgZ2V0KFxuICAgIHBsdWdpbjogc3RyaW5nLFxuICAgIGtleTogc3RyaW5nXG4gICk6IFByb21pc2U8e1xuICAgIGNvbXBvc2l0ZTogUGFydGlhbEpTT05WYWx1ZSB8IHVuZGVmaW5lZDtcbiAgICB1c2VyOiBQYXJ0aWFsSlNPTlZhbHVlIHwgdW5kZWZpbmVkO1xuICB9PiB7XG4gICAgLy8gV2FpdCBmb3IgZGF0YSBwcmVsb2FkIGJlZm9yZSBhbGxvd2luZyBub3JtYWwgb3BlcmF0aW9uLlxuICAgIGF3YWl0IHRoaXMuX3JlYWR5O1xuXG4gICAgY29uc3QgcGx1Z2lucyA9IHRoaXMucGx1Z2lucztcblxuICAgIGlmIChwbHVnaW4gaW4gcGx1Z2lucykge1xuICAgICAgY29uc3QgeyBjb21wb3NpdGUsIHVzZXIgfSA9IHBsdWdpbnNbcGx1Z2luXS5kYXRhO1xuXG4gICAgICByZXR1cm4ge1xuICAgICAgICBjb21wb3NpdGU6XG4gICAgICAgICAgY29tcG9zaXRlW2tleV0gIT09IHVuZGVmaW5lZCA/IGNvcHkoY29tcG9zaXRlW2tleV0hKSA6IHVuZGVmaW5lZCxcbiAgICAgICAgdXNlcjogdXNlcltrZXldICE9PSB1bmRlZmluZWQgPyBjb3B5KHVzZXJba2V5XSEpIDogdW5kZWZpbmVkXG4gICAgICB9O1xuICAgIH1cblxuICAgIHJldHVybiB0aGlzLmxvYWQocGx1Z2luKS50aGVuKCgpID0+IHRoaXMuZ2V0KHBsdWdpbiwga2V5KSk7XG4gIH1cblxuICAvKipcbiAgICogTG9hZCBhIHBsdWdpbidzIHNldHRpbmdzIGludG8gdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAqXG4gICAqIEBwYXJhbSBwbHVnaW4gLSBUaGUgbmFtZSBvZiB0aGUgcGx1Z2luIHdob3NlIHNldHRpbmdzIGFyZSBiZWluZyBsb2FkZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdpdGggYSBwbHVnaW4gc2V0dGluZ3Mgb2JqZWN0IG9yIHJlamVjdHNcbiAgICogaWYgdGhlIHBsdWdpbiBpcyBub3QgZm91bmQuXG4gICAqL1xuICBhc3luYyBsb2FkKHBsdWdpbjogc3RyaW5nKTogUHJvbWlzZTxJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncz4ge1xuICAgIC8vIFdhaXQgZm9yIGRhdGEgcHJlbG9hZCBiZWZvcmUgYWxsb3dpbmcgbm9ybWFsIG9wZXJhdGlvbi5cbiAgICBhd2FpdCB0aGlzLl9yZWFkeTtcblxuICAgIGNvbnN0IHBsdWdpbnMgPSB0aGlzLnBsdWdpbnM7XG4gICAgY29uc3QgcmVnaXN0cnkgPSB0aGlzOyAvLyBlc2xpbnQtZGlzYWJsZS1saW5lXG5cbiAgICAvLyBJZiB0aGUgcGx1Z2luIGV4aXN0cywgcmVzb2x2ZS5cbiAgICBpZiAocGx1Z2luIGluIHBsdWdpbnMpIHtcbiAgICAgIHJldHVybiBuZXcgU2V0dGluZ3MoeyBwbHVnaW46IHBsdWdpbnNbcGx1Z2luXSwgcmVnaXN0cnkgfSk7XG4gICAgfVxuXG4gICAgLy8gSWYgdGhlIHBsdWdpbiBuZWVkcyB0byBiZSBsb2FkZWQgZnJvbSB0aGUgZGF0YSBjb25uZWN0b3IsIGZldGNoLlxuICAgIHJldHVybiB0aGlzLnJlbG9hZChwbHVnaW4pO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbG9hZCBhIHBsdWdpbidzIHNldHRpbmdzIGludG8gdGhlIHJlZ2lzdHJ5IGV2ZW4gaWYgdGhleSBhbHJlYWR5IGV4aXN0LlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIG5hbWUgb2YgdGhlIHBsdWdpbiB3aG9zZSBzZXR0aW5ncyBhcmUgYmVpbmcgcmVsb2FkZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdpdGggYSBwbHVnaW4gc2V0dGluZ3Mgb2JqZWN0IG9yIHJlamVjdHNcbiAgICogd2l0aCBhIGxpc3Qgb2YgYElTY2hlbWFWYWxpZGF0b3IuSUVycm9yYCBvYmplY3RzIGlmIGl0IGZhaWxzLlxuICAgKi9cbiAgYXN5bmMgcmVsb2FkKHBsdWdpbjogc3RyaW5nKTogUHJvbWlzZTxJU2V0dGluZ1JlZ2lzdHJ5LklTZXR0aW5ncz4ge1xuICAgIC8vIFdhaXQgZm9yIGRhdGEgcHJlbG9hZCBiZWZvcmUgYWxsb3dpbmcgbm9ybWFsIG9wZXJhdGlvbi5cbiAgICBhd2FpdCB0aGlzLl9yZWFkeTtcblxuICAgIGNvbnN0IGZldGNoZWQgPSBhd2FpdCB0aGlzLmNvbm5lY3Rvci5mZXRjaChwbHVnaW4pO1xuICAgIGNvbnN0IHBsdWdpbnMgPSB0aGlzLnBsdWdpbnM7IC8vIGVzbGludC1kaXNhYmxlLWxpbmVcbiAgICBjb25zdCByZWdpc3RyeSA9IHRoaXM7IC8vIGVzbGludC1kaXNhYmxlLWxpbmVcblxuICAgIGlmIChmZXRjaGVkID09PSB1bmRlZmluZWQpIHtcbiAgICAgIHRocm93IFtcbiAgICAgICAge1xuICAgICAgICAgIGRhdGFQYXRoOiAnJyxcbiAgICAgICAgICBrZXl3b3JkOiAnaWQnLFxuICAgICAgICAgIG1lc3NhZ2U6IGBDb3VsZCBub3QgZmV0Y2ggc2V0dGluZ3MgZm9yICR7cGx1Z2lufS5gLFxuICAgICAgICAgIHNjaGVtYVBhdGg6ICcnXG4gICAgICAgIH0gYXMgSVNjaGVtYVZhbGlkYXRvci5JRXJyb3JcbiAgICAgIF07XG4gICAgfVxuICAgIGF3YWl0IHRoaXMuX2xvYWQoYXdhaXQgdGhpcy5fdHJhbnNmb3JtKCdmZXRjaCcsIGZldGNoZWQpKTtcbiAgICB0aGlzLl9wbHVnaW5DaGFuZ2VkLmVtaXQocGx1Z2luKTtcblxuICAgIHJldHVybiBuZXcgU2V0dGluZ3MoeyBwbHVnaW46IHBsdWdpbnNbcGx1Z2luXSwgcmVnaXN0cnkgfSk7XG4gIH1cblxuICAvKipcbiAgICogUmVtb3ZlIGEgc2luZ2xlIHNldHRpbmcgaW4gdGhlIHJlZ2lzdHJ5LlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIG5hbWUgb2YgdGhlIHBsdWdpbiB3aG9zZSBzZXR0aW5nIGlzIGJlaW5nIHJlbW92ZWQuXG4gICAqXG4gICAqIEBwYXJhbSBrZXkgLSBUaGUgbmFtZSBvZiB0aGUgc2V0dGluZyBiZWluZyByZW1vdmVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBzZXR0aW5nIGlzIHJlbW92ZWQuXG4gICAqL1xuICBhc3luYyByZW1vdmUocGx1Z2luOiBzdHJpbmcsIGtleTogc3RyaW5nKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgLy8gV2FpdCBmb3IgZGF0YSBwcmVsb2FkIGJlZm9yZSBhbGxvd2luZyBub3JtYWwgb3BlcmF0aW9uLlxuICAgIGF3YWl0IHRoaXMuX3JlYWR5O1xuXG4gICAgY29uc3QgcGx1Z2lucyA9IHRoaXMucGx1Z2lucztcblxuICAgIGlmICghKHBsdWdpbiBpbiBwbHVnaW5zKSkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIGNvbnN0IHJhdyA9IGpzb241LnBhcnNlKHBsdWdpbnNbcGx1Z2luXS5yYXcpO1xuXG4gICAgLy8gRGVsZXRlIGJvdGggdGhlIHZhbHVlIGFuZCBhbnkgYXNzb2NpYXRlZCBjb21tZW50LlxuICAgIGRlbGV0ZSByYXdba2V5XTtcbiAgICBkZWxldGUgcmF3W2AvLyAke2tleX1gXTtcbiAgICBwbHVnaW5zW3BsdWdpbl0ucmF3ID0gUHJpdmF0ZS5hbm5vdGF0ZWRQbHVnaW4ocGx1Z2luc1twbHVnaW5dLCByYXcpO1xuXG4gICAgcmV0dXJuIHRoaXMuX3NhdmUocGx1Z2luKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTZXQgYSBzaW5nbGUgc2V0dGluZyBpbiB0aGUgcmVnaXN0cnkuXG4gICAqXG4gICAqIEBwYXJhbSBwbHVnaW4gLSBUaGUgbmFtZSBvZiB0aGUgcGx1Z2luIHdob3NlIHNldHRpbmcgaXMgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcGFyYW0gdmFsdWUgLSBUaGUgdmFsdWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBzZXR0aW5nIGhhcyBiZWVuIHNhdmVkLlxuICAgKlxuICAgKi9cbiAgYXN5bmMgc2V0KHBsdWdpbjogc3RyaW5nLCBrZXk6IHN0cmluZywgdmFsdWU6IEpTT05WYWx1ZSk6IFByb21pc2U8dm9pZD4ge1xuICAgIC8vIFdhaXQgZm9yIGRhdGEgcHJlbG9hZCBiZWZvcmUgYWxsb3dpbmcgbm9ybWFsIG9wZXJhdGlvbi5cbiAgICBhd2FpdCB0aGlzLl9yZWFkeTtcblxuICAgIGNvbnN0IHBsdWdpbnMgPSB0aGlzLnBsdWdpbnM7XG5cbiAgICBpZiAoIShwbHVnaW4gaW4gcGx1Z2lucykpIHtcbiAgICAgIHJldHVybiB0aGlzLmxvYWQocGx1Z2luKS50aGVuKCgpID0+IHRoaXMuc2V0KHBsdWdpbiwga2V5LCB2YWx1ZSkpO1xuICAgIH1cblxuICAgIC8vIFBhcnNlIHRoZSByYXcgSlNPTiBzdHJpbmcgcmVtb3ZpbmcgYWxsIGNvbW1lbnRzIGFuZCByZXR1cm4gYW4gb2JqZWN0LlxuICAgIGNvbnN0IHJhdyA9IGpzb241LnBhcnNlKHBsdWdpbnNbcGx1Z2luXS5yYXcpO1xuXG4gICAgcGx1Z2luc1twbHVnaW5dLnJhdyA9IFByaXZhdGUuYW5ub3RhdGVkUGx1Z2luKHBsdWdpbnNbcGx1Z2luXSwge1xuICAgICAgLi4ucmF3LFxuICAgICAgW2tleV06IHZhbHVlXG4gICAgfSk7XG5cbiAgICByZXR1cm4gdGhpcy5fc2F2ZShwbHVnaW4pO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlZ2lzdGVyIGEgcGx1Z2luIHRyYW5zZm9ybSBmdW5jdGlvbiB0byBhY3Qgb24gYSBzcGVjaWZpYyBwbHVnaW4uXG4gICAqXG4gICAqIEBwYXJhbSBwbHVnaW4gLSBUaGUgbmFtZSBvZiB0aGUgcGx1Z2luIHdob3NlIHNldHRpbmdzIGFyZSB0cmFuc2Zvcm1lZC5cbiAgICpcbiAgICogQHBhcmFtIHRyYW5zZm9ybXMgLSBUaGUgdHJhbnNmb3JtIGZ1bmN0aW9ucyBhcHBsaWVkIHRvIHRoZSBwbHVnaW4uXG4gICAqXG4gICAqIEByZXR1cm5zIEEgZGlzcG9zYWJsZSB0aGF0IHJlbW92ZXMgdGhlIHRyYW5zZm9ybXMgZnJvbSB0aGUgcmVnaXN0cnkuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogLSBgY29tcG9zZWAgdHJhbnNmb3JtYXRpb25zOiBUaGUgcmVnaXN0cnkgYXV0b21hdGljYWxseSBvdmVyd3JpdGVzIGFcbiAgICogcGx1Z2luJ3MgZGVmYXVsdCB2YWx1ZXMgd2l0aCB1c2VyIG92ZXJyaWRlcywgYnV0IGEgcGx1Z2luIG1heSBpbnN0ZWFkIHdpc2hcbiAgICogdG8gbWVyZ2UgdmFsdWVzLiBUaGlzIGJlaGF2aW9yIGNhbiBiZSBhY2NvbXBsaXNoZWQgaW4gYSBgY29tcG9zZWBcbiAgICogdHJhbnNmb3JtYXRpb24uXG4gICAqIC0gYGZldGNoYCB0cmFuc2Zvcm1hdGlvbnM6IFRoZSByZWdpc3RyeSB1c2VzIHRoZSBwbHVnaW4gZGF0YSB0aGF0IGlzXG4gICAqIGZldGNoZWQgZnJvbSBpdHMgY29ubmVjdG9yLiBJZiBhIHBsdWdpbiB3YW50cyB0byBvdmVycmlkZSwgZS5nLiB0byB1cGRhdGVcbiAgICogaXRzIHNjaGVtYSB3aXRoIGR5bmFtaWMgZGVmYXVsdHMsIGEgYGZldGNoYCB0cmFuc2Zvcm1hdGlvbiBjYW4gYmUgYXBwbGllZC5cbiAgICovXG4gIHRyYW5zZm9ybShcbiAgICBwbHVnaW46IHN0cmluZyxcbiAgICB0cmFuc2Zvcm1zOiB7XG4gICAgICBbcGhhc2UgaW4gSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luLlBoYXNlXT86IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbi5UcmFuc2Zvcm07XG4gICAgfVxuICApOiBJRGlzcG9zYWJsZSB7XG4gICAgY29uc3QgdHJhbnNmb3JtZXJzID0gdGhpcy5fdHJhbnNmb3JtZXJzO1xuXG4gICAgaWYgKHBsdWdpbiBpbiB0cmFuc2Zvcm1lcnMpIHtcbiAgICAgIGNvbnN0IGVycm9yID0gbmV3IEVycm9yKGAke3BsdWdpbn0gYWxyZWFkeSBoYXMgYSB0cmFuc2Zvcm1lci5gKTtcbiAgICAgIGVycm9yLm5hbWUgPSAnVHJhbnNmb3JtRXJyb3InO1xuICAgICAgdGhyb3cgZXJyb3I7XG4gICAgfVxuXG4gICAgdHJhbnNmb3JtZXJzW3BsdWdpbl0gPSB7XG4gICAgICBmZXRjaDogdHJhbnNmb3Jtcy5mZXRjaCB8fCAocGx1Z2luID0+IHBsdWdpbiksXG4gICAgICBjb21wb3NlOiB0cmFuc2Zvcm1zLmNvbXBvc2UgfHwgKHBsdWdpbiA9PiBwbHVnaW4pXG4gICAgfTtcblxuICAgIHJldHVybiBuZXcgRGlzcG9zYWJsZURlbGVnYXRlKCgpID0+IHtcbiAgICAgIGRlbGV0ZSB0cmFuc2Zvcm1lcnNbcGx1Z2luXTtcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBVcGxvYWQgYSBwbHVnaW4ncyBzZXR0aW5ncy5cbiAgICpcbiAgICogQHBhcmFtIHBsdWdpbiAtIFRoZSBuYW1lIG9mIHRoZSBwbHVnaW4gd2hvc2Ugc2V0dGluZ3MgYXJlIGJlaW5nIHNldC5cbiAgICpcbiAgICogQHBhcmFtIHJhdyAtIFRoZSByYXcgcGx1Z2luIHNldHRpbmdzIGJlaW5nIHVwbG9hZGVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBzZXR0aW5ncyBoYXZlIGJlZW4gc2F2ZWQuXG4gICAqL1xuICBhc3luYyB1cGxvYWQocGx1Z2luOiBzdHJpbmcsIHJhdzogc3RyaW5nKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgLy8gV2FpdCBmb3IgZGF0YSBwcmVsb2FkIGJlZm9yZSBhbGxvd2luZyBub3JtYWwgb3BlcmF0aW9uLlxuICAgIGF3YWl0IHRoaXMuX3JlYWR5O1xuXG4gICAgY29uc3QgcGx1Z2lucyA9IHRoaXMucGx1Z2lucztcblxuICAgIGlmICghKHBsdWdpbiBpbiBwbHVnaW5zKSkge1xuICAgICAgcmV0dXJuIHRoaXMubG9hZChwbHVnaW4pLnRoZW4oKCkgPT4gdGhpcy51cGxvYWQocGx1Z2luLCByYXcpKTtcbiAgICB9XG5cbiAgICAvLyBTZXQgdGhlIGxvY2FsIGNvcHkuXG4gICAgcGx1Z2luc1twbHVnaW5dLnJhdyA9IHJhdztcblxuICAgIHJldHVybiB0aGlzLl9zYXZlKHBsdWdpbik7XG4gIH1cblxuICAvKipcbiAgICogTG9hZCBhIHBsdWdpbiBpbnRvIHRoZSByZWdpc3RyeS5cbiAgICovXG4gIHByaXZhdGUgYXN5bmMgX2xvYWQoZGF0YTogSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgY29uc3QgcGx1Z2luID0gZGF0YS5pZDtcblxuICAgIC8vIFZhbGlkYXRlIGFuZCBwcmVsb2FkIHRoZSBpdGVtLlxuICAgIHRyeSB7XG4gICAgICBhd2FpdCB0aGlzLl92YWxpZGF0ZShkYXRhKTtcbiAgICB9IGNhdGNoIChlcnJvcnMpIHtcbiAgICAgIGNvbnN0IG91dHB1dCA9IFtgVmFsaWRhdGluZyAke3BsdWdpbn0gZmFpbGVkOmBdO1xuXG4gICAgICAoZXJyb3JzIGFzIElTY2hlbWFWYWxpZGF0b3IuSUVycm9yW10pLmZvckVhY2goKGVycm9yLCBpbmRleCkgPT4ge1xuICAgICAgICBjb25zdCB7IGRhdGFQYXRoLCBzY2hlbWFQYXRoLCBrZXl3b3JkLCBtZXNzYWdlIH0gPSBlcnJvcjtcblxuICAgICAgICBpZiAoZGF0YVBhdGggfHwgc2NoZW1hUGF0aCkge1xuICAgICAgICAgIG91dHB1dC5wdXNoKGAke2luZGV4fSAtIHNjaGVtYSBAICR7c2NoZW1hUGF0aH0sIGRhdGEgQCAke2RhdGFQYXRofWApO1xuICAgICAgICB9XG4gICAgICAgIG91dHB1dC5wdXNoKGB7JHtrZXl3b3JkfX0gJHttZXNzYWdlfWApO1xuICAgICAgfSk7XG4gICAgICBjb25zb2xlLndhcm4ob3V0cHV0LmpvaW4oJ1xcbicpKTtcblxuICAgICAgdGhyb3cgZXJyb3JzO1xuICAgIH1cbiAgfVxuXG4gIC8qKlxuICAgKiBQcmVsb2FkIGEgbGlzdCBvZiBwbHVnaW5zIGFuZCBmYWlsIGdyYWNlZnVsbHkuXG4gICAqL1xuICBwcml2YXRlIGFzeW5jIF9wcmVsb2FkKHBsdWdpbnM6IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbltdKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgYXdhaXQgUHJvbWlzZS5hbGwoXG4gICAgICBwbHVnaW5zLm1hcChhc3luYyBwbHVnaW4gPT4ge1xuICAgICAgICB0cnkge1xuICAgICAgICAgIC8vIEFwcGx5IGEgdHJhbnNmb3JtYXRpb24gdG8gdGhlIHBsdWdpbiBpZiBuZWNlc3NhcnkuXG4gICAgICAgICAgYXdhaXQgdGhpcy5fbG9hZChhd2FpdCB0aGlzLl90cmFuc2Zvcm0oJ2ZldGNoJywgcGx1Z2luKSk7XG4gICAgICAgIH0gY2F0Y2ggKGVycm9ycykge1xuICAgICAgICAgIC8qIElnbm9yZSBwcmVsb2FkIHRpbWVvdXQgZXJyb3JzIHNpbGVudGx5LiAqL1xuICAgICAgICAgIGlmIChlcnJvcnNbMF0/LmtleXdvcmQgIT09ICd0aW1lb3V0Jykge1xuICAgICAgICAgICAgY29uc29sZS53YXJuKCdJZ25vcmVkIHNldHRpbmcgcmVnaXN0cnkgcHJlbG9hZCBlcnJvcnMuJywgZXJyb3JzKTtcbiAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICAgIH0pXG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBTYXZlIGEgcGx1Z2luIGluIHRoZSByZWdpc3RyeS5cbiAgICovXG4gIHByaXZhdGUgYXN5bmMgX3NhdmUocGx1Z2luOiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICBjb25zdCBwbHVnaW5zID0gdGhpcy5wbHVnaW5zO1xuXG4gICAgaWYgKCEocGx1Z2luIGluIHBsdWdpbnMpKSB7XG4gICAgICB0aHJvdyBuZXcgRXJyb3IoYCR7cGx1Z2lufSBkb2VzIG5vdCBleGlzdCBpbiBzZXR0aW5nIHJlZ2lzdHJ5LmApO1xuICAgIH1cblxuICAgIHRyeSB7XG4gICAgICBhd2FpdCB0aGlzLl92YWxpZGF0ZShwbHVnaW5zW3BsdWdpbl0pO1xuICAgIH0gY2F0Y2ggKGVycm9ycykge1xuICAgICAgY29uc29sZS53YXJuKGAke3BsdWdpbn0gdmFsaWRhdGlvbiBlcnJvcnM6YCwgZXJyb3JzKTtcbiAgICAgIHRocm93IG5ldyBFcnJvcihgJHtwbHVnaW59IGZhaWxlZCB0byB2YWxpZGF0ZTsgY2hlY2sgY29uc29sZS5gKTtcbiAgICB9XG4gICAgYXdhaXQgdGhpcy5jb25uZWN0b3Iuc2F2ZShwbHVnaW4sIHBsdWdpbnNbcGx1Z2luXS5yYXcpO1xuXG4gICAgLy8gRmV0Y2ggYW5kIHJlbG9hZCB0aGUgZGF0YSB0byBndWFyYW50ZWUgc2VydmVyIGFuZCBjbGllbnQgYXJlIGluIHN5bmMuXG4gICAgY29uc3QgZmV0Y2hlZCA9IGF3YWl0IHRoaXMuY29ubmVjdG9yLmZldGNoKHBsdWdpbik7XG4gICAgaWYgKGZldGNoZWQgPT09IHVuZGVmaW5lZCkge1xuICAgICAgdGhyb3cgW1xuICAgICAgICB7XG4gICAgICAgICAgZGF0YVBhdGg6ICcnLFxuICAgICAgICAgIGtleXdvcmQ6ICdpZCcsXG4gICAgICAgICAgbWVzc2FnZTogYENvdWxkIG5vdCBmZXRjaCBzZXR0aW5ncyBmb3IgJHtwbHVnaW59LmAsXG4gICAgICAgICAgc2NoZW1hUGF0aDogJydcbiAgICAgICAgfSBhcyBJU2NoZW1hVmFsaWRhdG9yLklFcnJvclxuICAgICAgXTtcbiAgICB9XG4gICAgYXdhaXQgdGhpcy5fbG9hZChhd2FpdCB0aGlzLl90cmFuc2Zvcm0oJ2ZldGNoJywgZmV0Y2hlZCkpO1xuICAgIHRoaXMuX3BsdWdpbkNoYW5nZWQuZW1pdChwbHVnaW4pO1xuICB9XG5cbiAgLyoqXG4gICAqIFRyYW5zZm9ybSB0aGUgcGx1Z2luIGlmIG5lY2Vzc2FyeS5cbiAgICovXG4gIHByaXZhdGUgYXN5bmMgX3RyYW5zZm9ybShcbiAgICBwaGFzZTogSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luLlBoYXNlLFxuICAgIHBsdWdpbjogSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luLFxuICAgIHN0YXJ0ZWQgPSBuZXcgRGF0ZSgpLmdldFRpbWUoKVxuICApOiBQcm9taXNlPElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbj4ge1xuICAgIGNvbnN0IGVsYXBzZWQgPSBuZXcgRGF0ZSgpLmdldFRpbWUoKSAtIHN0YXJ0ZWQ7XG4gICAgY29uc3QgaWQgPSBwbHVnaW4uaWQ7XG4gICAgY29uc3QgdHJhbnNmb3JtZXJzID0gdGhpcy5fdHJhbnNmb3JtZXJzO1xuICAgIGNvbnN0IHRpbWVvdXQgPSB0aGlzLl90aW1lb3V0O1xuXG4gICAgaWYgKCFwbHVnaW4uc2NoZW1hWydqdXB5dGVyLmxhYi50cmFuc2Zvcm0nXSkge1xuICAgICAgcmV0dXJuIHBsdWdpbjtcbiAgICB9XG5cbiAgICBpZiAoaWQgaW4gdHJhbnNmb3JtZXJzKSB7XG4gICAgICBjb25zdCB0cmFuc2Zvcm1lZCA9IHRyYW5zZm9ybWVyc1tpZF1bcGhhc2VdLmNhbGwobnVsbCwgcGx1Z2luKTtcblxuICAgICAgaWYgKHRyYW5zZm9ybWVkLmlkICE9PSBpZCkge1xuICAgICAgICB0aHJvdyBbXG4gICAgICAgICAge1xuICAgICAgICAgICAgZGF0YVBhdGg6ICcnLFxuICAgICAgICAgICAga2V5d29yZDogJ2lkJyxcbiAgICAgICAgICAgIG1lc3NhZ2U6ICdQbHVnaW4gdHJhbnNmb3JtYXRpb25zIGNhbm5vdCBjaGFuZ2UgcGx1Z2luIElEcy4nLFxuICAgICAgICAgICAgc2NoZW1hUGF0aDogJydcbiAgICAgICAgICB9IGFzIElTY2hlbWFWYWxpZGF0b3IuSUVycm9yXG4gICAgICAgIF07XG4gICAgICB9XG5cbiAgICAgIHJldHVybiB0cmFuc2Zvcm1lZDtcbiAgICB9XG5cbiAgICAvLyBJZiB0aGUgdGltZW91dCBoYXMgbm90IGJlZW4gZXhjZWVkZWQsIHN0YWxsIGFuZCB0cnkgYWdhaW4gaW4gMjUwbXMuXG4gICAgaWYgKGVsYXBzZWQgPCB0aW1lb3V0KSB7XG4gICAgICBhd2FpdCBuZXcgUHJvbWlzZTx2b2lkPihyZXNvbHZlID0+IHtcbiAgICAgICAgc2V0VGltZW91dCgoKSA9PiB7XG4gICAgICAgICAgcmVzb2x2ZSgpO1xuICAgICAgICB9LCAyNTApO1xuICAgICAgfSk7XG4gICAgICByZXR1cm4gdGhpcy5fdHJhbnNmb3JtKHBoYXNlLCBwbHVnaW4sIHN0YXJ0ZWQpO1xuICAgIH1cblxuICAgIHRocm93IFtcbiAgICAgIHtcbiAgICAgICAgZGF0YVBhdGg6ICcnLFxuICAgICAgICBrZXl3b3JkOiAndGltZW91dCcsXG4gICAgICAgIG1lc3NhZ2U6IGBUcmFuc2Zvcm1pbmcgJHtwbHVnaW4uaWR9IHRpbWVkIG91dC5gLFxuICAgICAgICBzY2hlbWFQYXRoOiAnJ1xuICAgICAgfSBhcyBJU2NoZW1hVmFsaWRhdG9yLklFcnJvclxuICAgIF07XG4gIH1cblxuICAvKipcbiAgICogVmFsaWRhdGUgYW5kIHByZWxvYWQgYSBwbHVnaW4sIGNvbXBvc2UgdGhlIGBjb21wb3NpdGVgIGRhdGEuXG4gICAqL1xuICBwcml2YXRlIGFzeW5jIF92YWxpZGF0ZShwbHVnaW46IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbik6IFByb21pc2U8dm9pZD4ge1xuICAgIC8vIFZhbGlkYXRlIHRoZSB1c2VyIGRhdGEgYW5kIGNyZWF0ZSB0aGUgY29tcG9zaXRlIGRhdGEuXG4gICAgY29uc3QgZXJyb3JzID0gdGhpcy52YWxpZGF0b3IudmFsaWRhdGVEYXRhKHBsdWdpbik7XG5cbiAgICBpZiAoZXJyb3JzKSB7XG4gICAgICB0aHJvdyBlcnJvcnM7XG4gICAgfVxuXG4gICAgLy8gQXBwbHkgYSB0cmFuc2Zvcm1hdGlvbiBpZiBuZWNlc3NhcnkgYW5kIHNldCB0aGUgbG9jYWwgY29weS5cbiAgICB0aGlzLnBsdWdpbnNbcGx1Z2luLmlkXSA9IGF3YWl0IHRoaXMuX3RyYW5zZm9ybSgnY29tcG9zZScsIHBsdWdpbik7XG4gIH1cblxuICBwcml2YXRlIF9wbHVnaW5DaGFuZ2VkID0gbmV3IFNpZ25hbDx0aGlzLCBzdHJpbmc+KHRoaXMpO1xuICBwcml2YXRlIF9yZWFkeSA9IFByb21pc2UucmVzb2x2ZSgpO1xuICBwcml2YXRlIF90aW1lb3V0OiBudW1iZXI7XG4gIHByaXZhdGUgX3RyYW5zZm9ybWVyczoge1xuICAgIFtwbHVnaW46IHN0cmluZ106IHtcbiAgICAgIFtwaGFzZSBpbiBJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW4uUGhhc2VdOiBJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW4uVHJhbnNmb3JtO1xuICAgIH07XG4gIH0gPSBPYmplY3QuY3JlYXRlKG51bGwpO1xufVxuXG4vKipcbiAqIEEgbWFuYWdlciBmb3IgYSBzcGVjaWZpYyBwbHVnaW4ncyBzZXR0aW5ncy5cbiAqL1xuZXhwb3J0IGNsYXNzIFNldHRpbmdzIGltcGxlbWVudHMgSVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3Mge1xuICAvKipcbiAgICogSW5zdGFudGlhdGUgYSBuZXcgcGx1Z2luIHNldHRpbmdzIG1hbmFnZXIuXG4gICAqL1xuICBjb25zdHJ1Y3RvcihvcHRpb25zOiBTZXR0aW5ncy5JT3B0aW9ucykge1xuICAgIHRoaXMuaWQgPSBvcHRpb25zLnBsdWdpbi5pZDtcbiAgICB0aGlzLnJlZ2lzdHJ5ID0gb3B0aW9ucy5yZWdpc3RyeTtcbiAgICB0aGlzLnJlZ2lzdHJ5LnBsdWdpbkNoYW5nZWQuY29ubmVjdCh0aGlzLl9vblBsdWdpbkNoYW5nZWQsIHRoaXMpO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBwbHVnaW4gbmFtZS5cbiAgICovXG4gIHJlYWRvbmx5IGlkOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFRoZSBzZXR0aW5nIHJlZ2lzdHJ5IGluc3RhbmNlIHVzZWQgYXMgYSBiYWNrLWVuZCBmb3IgdGhlc2Ugc2V0dGluZ3MuXG4gICAqL1xuICByZWFkb25seSByZWdpc3RyeTogSVNldHRpbmdSZWdpc3RyeTtcblxuICAvKipcbiAgICogQSBzaWduYWwgdGhhdCBlbWl0cyB3aGVuIHRoZSBwbHVnaW4ncyBzZXR0aW5ncyBoYXZlIGNoYW5nZWQuXG4gICAqL1xuICBnZXQgY2hhbmdlZCgpOiBJU2lnbmFsPHRoaXMsIHZvaWQ+IHtcbiAgICByZXR1cm4gdGhpcy5fY2hhbmdlZDtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgY29tcG9zaXRlIG9mIHVzZXIgc2V0dGluZ3MgYW5kIGV4dGVuc2lvbiBkZWZhdWx0cy5cbiAgICovXG4gIGdldCBjb21wb3NpdGUoKTogUmVhZG9ubHlQYXJ0aWFsSlNPTk9iamVjdCB7XG4gICAgcmV0dXJuIHRoaXMucGx1Z2luLmRhdGEuY29tcG9zaXRlO1xuICB9XG5cbiAgLyoqXG4gICAqIFRlc3Qgd2hldGhlciB0aGUgcGx1Z2luIHNldHRpbmdzIG1hbmFnZXIgZGlzcG9zZWQuXG4gICAqL1xuICBnZXQgaXNEaXNwb3NlZCgpOiBib29sZWFuIHtcbiAgICByZXR1cm4gdGhpcy5faXNEaXNwb3NlZDtcbiAgfVxuXG4gIGdldCBwbHVnaW4oKTogSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luIHtcbiAgICByZXR1cm4gdGhpcy5yZWdpc3RyeS5wbHVnaW5zW3RoaXMuaWRdITtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgcGx1Z2luJ3Mgc2NoZW1hLlxuICAgKi9cbiAgZ2V0IHNjaGVtYSgpOiBJU2V0dGluZ1JlZ2lzdHJ5LklTY2hlbWEge1xuICAgIHJldHVybiB0aGlzLnBsdWdpbi5zY2hlbWE7XG4gIH1cblxuICAvKipcbiAgICogVGhlIHBsdWdpbiBzZXR0aW5ncyByYXcgdGV4dCB2YWx1ZS5cbiAgICovXG4gIGdldCByYXcoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5wbHVnaW4ucmF3O1xuICB9XG5cbiAgLyoqXG4gICAqIENoZWNrcyBpZiBhbnkgZmllbGRzIGFyZSBkaWZmZXJlbnQgZnJvbSB0aGUgZGVmYXVsdCB2YWx1ZS5cbiAgICovXG4gIGlzRGVmYXVsdCh1c2VyOiBSZWFkb25seVBhcnRpYWxKU09OT2JqZWN0KTogYm9vbGVhbiB7XG4gICAgZm9yIChjb25zdCBrZXkgaW4gdGhpcy5zY2hlbWEucHJvcGVydGllcykge1xuICAgICAgY29uc3QgdmFsdWUgPSB1c2VyW2tleV07XG4gICAgICBjb25zdCBkZWZhdWx0VmFsdWUgPSB0aGlzLmRlZmF1bHQoa2V5KTtcbiAgICAgIGlmIChcbiAgICAgICAgdmFsdWUgPT09IHVuZGVmaW5lZCB8fFxuICAgICAgICBkZWZhdWx0VmFsdWUgPT09IHVuZGVmaW5lZCB8fFxuICAgICAgICBKU09ORXh0LmRlZXBFcXVhbCh2YWx1ZSwgSlNPTkV4dC5lbXB0eU9iamVjdCkgfHxcbiAgICAgICAgSlNPTkV4dC5kZWVwRXF1YWwodmFsdWUsIEpTT05FeHQuZW1wdHlBcnJheSlcbiAgICAgICkge1xuICAgICAgICBjb250aW51ZTtcbiAgICAgIH1cbiAgICAgIGlmICghSlNPTkV4dC5kZWVwRXF1YWwodmFsdWUsIGRlZmF1bHRWYWx1ZSkpIHtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gdHJ1ZTtcbiAgfVxuXG4gIGdldCBpc01vZGlmaWVkKCk6IGJvb2xlYW4ge1xuICAgIHJldHVybiAhdGhpcy5pc0RlZmF1bHQodGhpcy51c2VyKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgdXNlciBzZXR0aW5ncy5cbiAgICovXG4gIGdldCB1c2VyKCk6IFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3Qge1xuICAgIHJldHVybiB0aGlzLnBsdWdpbi5kYXRhLnVzZXI7XG4gIH1cblxuICAvKipcbiAgICogVGhlIHB1Ymxpc2hlZCB2ZXJzaW9uIG9mIHRoZSBOUE0gcGFja2FnZSBjb250YWluaW5nIHRoZXNlIHNldHRpbmdzLlxuICAgKi9cbiAgZ2V0IHZlcnNpb24oKTogc3RyaW5nIHtcbiAgICByZXR1cm4gdGhpcy5wbHVnaW4udmVyc2lvbjtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXR1cm4gdGhlIGRlZmF1bHRzIGluIGEgY29tbWVudGVkIEpTT04gZm9ybWF0LlxuICAgKi9cbiAgYW5ub3RhdGVkRGVmYXVsdHMoKTogc3RyaW5nIHtcbiAgICByZXR1cm4gUHJpdmF0ZS5hbm5vdGF0ZWREZWZhdWx0cyh0aGlzLnNjaGVtYSwgdGhpcy5pZCk7XG4gIH1cblxuICAvKipcbiAgICogQ2FsY3VsYXRlIHRoZSBkZWZhdWx0IHZhbHVlIG9mIGEgc2V0dGluZyBieSBpdGVyYXRpbmcgdGhyb3VnaCB0aGUgc2NoZW1hLlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgd2hvc2UgZGVmYXVsdCB2YWx1ZSBpcyBjYWxjdWxhdGVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIGNhbGN1bGF0ZWQgZGVmYXVsdCBKU09OIHZhbHVlIGZvciBhIHNwZWNpZmljIHNldHRpbmcuXG4gICAqL1xuICBkZWZhdWx0KGtleT86IHN0cmluZyk6IFBhcnRpYWxKU09OVmFsdWUgfCB1bmRlZmluZWQge1xuICAgIHJldHVybiBQcml2YXRlLnJlaWZ5RGVmYXVsdCh0aGlzLnNjaGVtYSwga2V5KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBEaXNwb3NlIG9mIHRoZSBwbHVnaW4gc2V0dGluZ3MgcmVzb3VyY2VzLlxuICAgKi9cbiAgZGlzcG9zZSgpOiB2b2lkIHtcbiAgICBpZiAodGhpcy5faXNEaXNwb3NlZCkge1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHRoaXMuX2lzRGlzcG9zZWQgPSB0cnVlO1xuICAgIFNpZ25hbC5jbGVhckRhdGEodGhpcyk7XG4gIH1cblxuICAvKipcbiAgICogR2V0IGFuIGluZGl2aWR1YWwgc2V0dGluZy5cbiAgICpcbiAgICogQHBhcmFtIGtleSAtIFRoZSBuYW1lIG9mIHRoZSBzZXR0aW5nIGJlaW5nIHJldHJpZXZlZC5cbiAgICpcbiAgICogQHJldHVybnMgVGhlIHNldHRpbmcgdmFsdWUuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBtZXRob2QgcmV0dXJucyBzeW5jaHJvbm91c2x5IGJlY2F1c2UgaXQgdXNlcyBhIGNhY2hlZCBjb3B5IG9mIHRoZVxuICAgKiBwbHVnaW4gc2V0dGluZ3MgdGhhdCBpcyBzeW5jaHJvbml6ZWQgd2l0aCB0aGUgcmVnaXN0cnkuXG4gICAqL1xuICBnZXQoa2V5OiBzdHJpbmcpOiB7XG4gICAgY29tcG9zaXRlOiBSZWFkb25seVBhcnRpYWxKU09OVmFsdWUgfCB1bmRlZmluZWQ7XG4gICAgdXNlcjogUmVhZG9ubHlQYXJ0aWFsSlNPTlZhbHVlIHwgdW5kZWZpbmVkO1xuICB9IHtcbiAgICBjb25zdCB7IGNvbXBvc2l0ZSwgdXNlciB9ID0gdGhpcztcblxuICAgIHJldHVybiB7XG4gICAgICBjb21wb3NpdGU6XG4gICAgICAgIGNvbXBvc2l0ZVtrZXldICE9PSB1bmRlZmluZWQgPyBjb3B5KGNvbXBvc2l0ZVtrZXldISkgOiB1bmRlZmluZWQsXG4gICAgICB1c2VyOiB1c2VyW2tleV0gIT09IHVuZGVmaW5lZCA/IGNvcHkodXNlcltrZXldISkgOiB1bmRlZmluZWRcbiAgICB9O1xuICB9XG5cbiAgLyoqXG4gICAqIFJlbW92ZSBhIHNpbmdsZSBzZXR0aW5nLlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgcmVtb3ZlZC5cbiAgICpcbiAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2hlbiB0aGUgc2V0dGluZyBpcyByZW1vdmVkLlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIFRoaXMgZnVuY3Rpb24gaXMgYXN5bmNocm9ub3VzIGJlY2F1c2UgaXQgd3JpdGVzIHRvIHRoZSBzZXR0aW5nIHJlZ2lzdHJ5LlxuICAgKi9cbiAgcmVtb3ZlKGtleTogc3RyaW5nKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMucmVnaXN0cnkucmVtb3ZlKHRoaXMucGx1Z2luLmlkLCBrZXkpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNhdmUgYWxsIG9mIHRoZSBwbHVnaW4ncyB1c2VyIHNldHRpbmdzIGF0IG9uY2UuXG4gICAqL1xuICBzYXZlKHJhdzogc3RyaW5nKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgcmV0dXJuIHRoaXMucmVnaXN0cnkudXBsb2FkKHRoaXMucGx1Z2luLmlkLCByYXcpO1xuICB9XG5cbiAgLyoqXG4gICAqIFNldCBhIHNpbmdsZSBzZXR0aW5nLlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcGFyYW0gdmFsdWUgLSBUaGUgdmFsdWUgb2YgdGhlIHNldHRpbmcuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIHNldHRpbmcgaGFzIGJlZW4gc2F2ZWQuXG4gICAqXG4gICAqICMjIyMgTm90ZXNcbiAgICogVGhpcyBmdW5jdGlvbiBpcyBhc3luY2hyb25vdXMgYmVjYXVzZSBpdCB3cml0ZXMgdG8gdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAqL1xuICBzZXQoa2V5OiBzdHJpbmcsIHZhbHVlOiBKU09OVmFsdWUpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICByZXR1cm4gdGhpcy5yZWdpc3RyeS5zZXQodGhpcy5wbHVnaW4uaWQsIGtleSwgdmFsdWUpO1xuICB9XG5cbiAgLyoqXG4gICAqIFZhbGlkYXRlcyByYXcgc2V0dGluZ3Mgd2l0aCBjb21tZW50cy5cbiAgICpcbiAgICogQHBhcmFtIHJhdyAtIFRoZSBKU09OIHdpdGggY29tbWVudHMgc3RyaW5nIGJlaW5nIHZhbGlkYXRlZC5cbiAgICpcbiAgICogQHJldHVybnMgQSBsaXN0IG9mIGVycm9ycyBvciBgbnVsbGAgaWYgdmFsaWQuXG4gICAqL1xuICB2YWxpZGF0ZShyYXc6IHN0cmluZyk6IElTY2hlbWFWYWxpZGF0b3IuSUVycm9yW10gfCBudWxsIHtcbiAgICBjb25zdCBkYXRhID0geyBjb21wb3NpdGU6IHt9LCB1c2VyOiB7fSB9O1xuICAgIGNvbnN0IHsgaWQsIHNjaGVtYSB9ID0gdGhpcy5wbHVnaW47XG4gICAgY29uc3QgdmFsaWRhdG9yID0gdGhpcy5yZWdpc3RyeS52YWxpZGF0b3I7XG4gICAgY29uc3QgdmVyc2lvbiA9IHRoaXMudmVyc2lvbjtcblxuICAgIHJldHVybiB2YWxpZGF0b3IudmFsaWRhdGVEYXRhKHsgZGF0YSwgaWQsIHJhdywgc2NoZW1hLCB2ZXJzaW9uIH0sIGZhbHNlKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBIYW5kbGUgcGx1Z2luIGNoYW5nZXMgaW4gdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAqL1xuICBwcml2YXRlIF9vblBsdWdpbkNoYW5nZWQoc2VuZGVyOiBhbnksIHBsdWdpbjogc3RyaW5nKTogdm9pZCB7XG4gICAgaWYgKHBsdWdpbiA9PT0gdGhpcy5wbHVnaW4uaWQpIHtcbiAgICAgIHRoaXMuX2NoYW5nZWQuZW1pdCh1bmRlZmluZWQpO1xuICAgIH1cbiAgfVxuXG4gIHByaXZhdGUgX2NoYW5nZWQgPSBuZXcgU2lnbmFsPHRoaXMsIHZvaWQ+KHRoaXMpO1xuICBwcml2YXRlIF9pc0Rpc3Bvc2VkID0gZmFsc2U7XG59XG5cbi8qKlxuICogQSBuYW1lc3BhY2UgZm9yIGBTZXR0aW5nUmVnaXN0cnlgIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgU2V0dGluZ1JlZ2lzdHJ5IHtcbiAgLyoqXG4gICAqIFRoZSBpbnN0YW50aWF0aW9uIG9wdGlvbnMgZm9yIGEgc2V0dGluZyByZWdpc3RyeVxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJT3B0aW9ucyB7XG4gICAgLyoqXG4gICAgICogVGhlIGRhdGEgY29ubmVjdG9yIHVzZWQgYnkgdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAgICovXG4gICAgY29ubmVjdG9yOiBJRGF0YUNvbm5lY3RvcjxJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW4sIHN0cmluZz47XG5cbiAgICAvKipcbiAgICAgKiBQcmVsb2FkZWQgcGx1Z2luIGRhdGEgdG8gcG9wdWxhdGUgdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAgICovXG4gICAgcGx1Z2lucz86IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbltdO1xuXG4gICAgLyoqXG4gICAgICogVGhlIG51bWJlciBvZiBtaWxsaXNlY29uZHMgYmVmb3JlIGEgYGxvYWQoKWAgY2FsbCB0byB0aGUgcmVnaXN0cnkgd2FpdHNcbiAgICAgKiBiZWZvcmUgdGltaW5nIG91dCBpZiBpdCByZXF1aXJlcyBhIHRyYW5zZm9ybWF0aW9uIHRoYXQgaGFzIG5vdCBiZWVuXG4gICAgICogcmVnaXN0ZXJlZC5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGUgZGVmYXVsdCB2YWx1ZSBpcyA3MDAwLlxuICAgICAqL1xuICAgIHRpbWVvdXQ/OiBudW1iZXI7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgdmFsaWRhdG9yIHVzZWQgdG8gZW5mb3JjZSB0aGUgc2V0dGluZ3MgSlNPTiBzY2hlbWEuXG4gICAgICovXG4gICAgdmFsaWRhdG9yPzogSVNjaGVtYVZhbGlkYXRvcjtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZWNvbmNpbGUgdGhlIG1lbnVzLlxuICAgKlxuICAgKiBAcGFyYW0gcmVmZXJlbmNlIFRoZSByZWZlcmVuY2UgbGlzdCBvZiBtZW51cy5cbiAgICogQHBhcmFtIGFkZGl0aW9uIFRoZSBsaXN0IG9mIG1lbnVzIHRvIGFkZC5cbiAgICogQHBhcmFtIHdhcm4gV2FybiBpZiB0aGUgY29tbWFuZCBpdGVtcyBhcmUgZHVwbGljYXRlZCB3aXRoaW4gdGhlIHNhbWUgbWVudS5cbiAgICogQHJldHVybnMgVGhlIHJlY29uY2lsZWQgbGlzdCBvZiBtZW51cy5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiByZWNvbmNpbGVNZW51cyhcbiAgICByZWZlcmVuY2U6IElTZXR0aW5nUmVnaXN0cnkuSU1lbnVbXSB8IG51bGwsXG4gICAgYWRkaXRpb246IElTZXR0aW5nUmVnaXN0cnkuSU1lbnVbXSB8IG51bGwsXG4gICAgd2FybjogYm9vbGVhbiA9IGZhbHNlLFxuICAgIGFkZE5ld0l0ZW1zOiBib29sZWFuID0gdHJ1ZVxuICApOiBJU2V0dGluZ1JlZ2lzdHJ5LklNZW51W10ge1xuICAgIGlmICghcmVmZXJlbmNlKSB7XG4gICAgICByZXR1cm4gYWRkaXRpb24gJiYgYWRkTmV3SXRlbXMgPyBKU09ORXh0LmRlZXBDb3B5KGFkZGl0aW9uKSA6IFtdO1xuICAgIH1cbiAgICBpZiAoIWFkZGl0aW9uKSB7XG4gICAgICByZXR1cm4gSlNPTkV4dC5kZWVwQ29weShyZWZlcmVuY2UpO1xuICAgIH1cblxuICAgIGNvbnN0IG1lcmdlZCA9IEpTT05FeHQuZGVlcENvcHkocmVmZXJlbmNlKTtcblxuICAgIGFkZGl0aW9uLmZvckVhY2gobWVudSA9PiB7XG4gICAgICBjb25zdCByZWZJbmRleCA9IG1lcmdlZC5maW5kSW5kZXgocmVmID0+IHJlZi5pZCA9PT0gbWVudS5pZCk7XG4gICAgICBpZiAocmVmSW5kZXggPj0gMCkge1xuICAgICAgICBtZXJnZWRbcmVmSW5kZXhdID0ge1xuICAgICAgICAgIC4uLm1lcmdlZFtyZWZJbmRleF0sXG4gICAgICAgICAgLi4ubWVudSxcbiAgICAgICAgICBpdGVtczogcmVjb25jaWxlSXRlbXMoXG4gICAgICAgICAgICBtZXJnZWRbcmVmSW5kZXhdLml0ZW1zLFxuICAgICAgICAgICAgbWVudS5pdGVtcyxcbiAgICAgICAgICAgIHdhcm4sXG4gICAgICAgICAgICBhZGROZXdJdGVtc1xuICAgICAgICAgIClcbiAgICAgICAgfTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGlmIChhZGROZXdJdGVtcykge1xuICAgICAgICAgIG1lcmdlZC5wdXNoKG1lbnUpO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG5cbiAgICByZXR1cm4gbWVyZ2VkO1xuICB9XG5cbiAgLyoqXG4gICAqIE1lcmdlIHR3byBzZXQgb2YgbWVudSBpdGVtcy5cbiAgICpcbiAgICogQHBhcmFtIHJlZmVyZW5jZSBSZWZlcmVuY2Ugc2V0IG9mIG1lbnUgaXRlbXNcbiAgICogQHBhcmFtIGFkZGl0aW9uIE5ldyBpdGVtcyB0byBhZGRcbiAgICogQHBhcmFtIHdhcm4gV2hldGhlciB0byB3YXJuIGlmIGl0ZW0gaXMgZHVwbGljYXRlZDsgZGVmYXVsdCB0byBmYWxzZVxuICAgKiBAcmV0dXJucyBUaGUgbWVyZ2VkIHNldCBvZiBpdGVtc1xuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIHJlY29uY2lsZUl0ZW1zPFQgZXh0ZW5kcyBJU2V0dGluZ1JlZ2lzdHJ5LklNZW51SXRlbT4oXG4gICAgcmVmZXJlbmNlPzogVFtdLFxuICAgIGFkZGl0aW9uPzogVFtdLFxuICAgIHdhcm46IGJvb2xlYW4gPSBmYWxzZSxcbiAgICBhZGROZXdJdGVtczogYm9vbGVhbiA9IHRydWVcbiAgKTogVFtdIHwgdW5kZWZpbmVkIHtcbiAgICBpZiAoIXJlZmVyZW5jZSkge1xuICAgICAgcmV0dXJuIGFkZGl0aW9uID8gSlNPTkV4dC5kZWVwQ29weShhZGRpdGlvbikgOiB1bmRlZmluZWQ7XG4gICAgfVxuICAgIGlmICghYWRkaXRpb24pIHtcbiAgICAgIHJldHVybiBKU09ORXh0LmRlZXBDb3B5KHJlZmVyZW5jZSk7XG4gICAgfVxuXG4gICAgY29uc3QgaXRlbXMgPSBKU09ORXh0LmRlZXBDb3B5KHJlZmVyZW5jZSk7XG5cbiAgICAvLyBNZXJnZSBhcnJheSBlbGVtZW50IGRlcGVuZGluZyBvbiB0aGUgdHlwZVxuICAgIGFkZGl0aW9uLmZvckVhY2goaXRlbSA9PiB7XG4gICAgICBzd2l0Y2ggKGl0ZW0udHlwZSA/PyAnY29tbWFuZCcpIHtcbiAgICAgICAgY2FzZSAnc2VwYXJhdG9yJzpcbiAgICAgICAgICBpZiAoYWRkTmV3SXRlbXMpIHtcbiAgICAgICAgICAgIGl0ZW1zLnB1c2goeyAuLi5pdGVtIH0pO1xuICAgICAgICAgIH1cbiAgICAgICAgICBicmVhaztcbiAgICAgICAgY2FzZSAnc3VibWVudSc6XG4gICAgICAgICAgaWYgKGl0ZW0uc3VibWVudSkge1xuICAgICAgICAgICAgY29uc3QgcmVmSW5kZXggPSBpdGVtcy5maW5kSW5kZXgoXG4gICAgICAgICAgICAgIHJlZiA9PlxuICAgICAgICAgICAgICAgIHJlZi50eXBlID09PSAnc3VibWVudScgJiYgcmVmLnN1Ym1lbnU/LmlkID09PSBpdGVtLnN1Ym1lbnU/LmlkXG4gICAgICAgICAgICApO1xuICAgICAgICAgICAgaWYgKHJlZkluZGV4IDwgMCkge1xuICAgICAgICAgICAgICBpZiAoYWRkTmV3SXRlbXMpIHtcbiAgICAgICAgICAgICAgICBpdGVtcy5wdXNoKEpTT05FeHQuZGVlcENvcHkoaXRlbSkpO1xuICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICBpdGVtc1tyZWZJbmRleF0gPSB7XG4gICAgICAgICAgICAgICAgLi4uaXRlbXNbcmVmSW5kZXhdLFxuICAgICAgICAgICAgICAgIC4uLml0ZW0sXG4gICAgICAgICAgICAgICAgc3VibWVudTogcmVjb25jaWxlTWVudXMoXG4gICAgICAgICAgICAgICAgICBpdGVtc1tyZWZJbmRleF0uc3VibWVudVxuICAgICAgICAgICAgICAgICAgICA/IFtpdGVtc1tyZWZJbmRleF0uc3VibWVudSBhcyBhbnldXG4gICAgICAgICAgICAgICAgICAgIDogbnVsbCxcbiAgICAgICAgICAgICAgICAgIFtpdGVtLnN1Ym1lbnVdLFxuICAgICAgICAgICAgICAgICAgd2FybixcbiAgICAgICAgICAgICAgICAgIGFkZE5ld0l0ZW1zXG4gICAgICAgICAgICAgICAgKVswXVxuICAgICAgICAgICAgICB9O1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH1cbiAgICAgICAgICBicmVhaztcbiAgICAgICAgY2FzZSAnY29tbWFuZCc6XG4gICAgICAgICAgaWYgKGl0ZW0uY29tbWFuZCkge1xuICAgICAgICAgICAgY29uc3QgcmVmSW5kZXggPSBpdGVtcy5maW5kSW5kZXgoXG4gICAgICAgICAgICAgIHJlZiA9PlxuICAgICAgICAgICAgICAgIHJlZi5jb21tYW5kID09PSBpdGVtLmNvbW1hbmQgJiZcbiAgICAgICAgICAgICAgICByZWYuc2VsZWN0b3IgPT09IGl0ZW0uc2VsZWN0b3IgJiZcbiAgICAgICAgICAgICAgICBKU09ORXh0LmRlZXBFcXVhbChyZWYuYXJncyA/PyB7fSwgaXRlbS5hcmdzID8/IHt9KVxuICAgICAgICAgICAgKTtcbiAgICAgICAgICAgIGlmIChyZWZJbmRleCA8IDApIHtcbiAgICAgICAgICAgICAgaWYgKGFkZE5ld0l0ZW1zKSB7XG4gICAgICAgICAgICAgICAgaXRlbXMucHVzaCh7IC4uLml0ZW0gfSk7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgIGlmICh3YXJuKSB7XG4gICAgICAgICAgICAgICAgY29uc29sZS53YXJuKFxuICAgICAgICAgICAgICAgICAgYE1lbnUgZW50cnkgZm9yIGNvbW1hbmQgJyR7aXRlbS5jb21tYW5kfScgaXMgZHVwbGljYXRlZC5gXG4gICAgICAgICAgICAgICAgKTtcbiAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICBpdGVtc1tyZWZJbmRleF0gPSB7IC4uLml0ZW1zW3JlZkluZGV4XSwgLi4uaXRlbSB9O1xuICAgICAgICAgICAgfVxuICAgICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcblxuICAgIHJldHVybiBpdGVtcztcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW1vdmUgZGlzYWJsZWQgZW50cmllcyBmcm9tIG1lbnUgaXRlbXNcbiAgICpcbiAgICogQHBhcmFtIGl0ZW1zIE1lbnUgaXRlbXNcbiAgICogQHJldHVybnMgRmlsdGVyZWQgbWVudSBpdGVtc1xuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGZpbHRlckRpc2FibGVkSXRlbXM8VCBleHRlbmRzIElTZXR0aW5nUmVnaXN0cnkuSU1lbnVJdGVtPihcbiAgICBpdGVtczogVFtdXG4gICk6IFRbXSB7XG4gICAgcmV0dXJuIGl0ZW1zLnJlZHVjZTxUW10+KChmaW5hbCwgdmFsdWUpID0+IHtcbiAgICAgIGNvbnN0IGNvcHkgPSB7IC4uLnZhbHVlIH07XG4gICAgICBpZiAoIWNvcHkuZGlzYWJsZWQpIHtcbiAgICAgICAgaWYgKGNvcHkudHlwZSA9PT0gJ3N1Ym1lbnUnKSB7XG4gICAgICAgICAgY29uc3QgeyBzdWJtZW51IH0gPSBjb3B5O1xuICAgICAgICAgIGlmIChzdWJtZW51ICYmICFzdWJtZW51LmRpc2FibGVkKSB7XG4gICAgICAgICAgICBjb3B5LnN1Ym1lbnUgPSB7XG4gICAgICAgICAgICAgIC4uLnN1Ym1lbnUsXG4gICAgICAgICAgICAgIGl0ZW1zOiBmaWx0ZXJEaXNhYmxlZEl0ZW1zKHN1Ym1lbnUuaXRlbXMgPz8gW10pXG4gICAgICAgICAgICB9O1xuICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgICAgICBmaW5hbC5wdXNoKGNvcHkpO1xuICAgICAgfVxuXG4gICAgICByZXR1cm4gZmluYWw7XG4gICAgfSwgW10pO1xuICB9XG5cbiAgLyoqXG4gICAqIFJlY29uY2lsZSBkZWZhdWx0IGFuZCB1c2VyIHNob3J0Y3V0cyBhbmQgcmV0dXJuIHRoZSBjb21wb3NpdGUgbGlzdC5cbiAgICpcbiAgICogQHBhcmFtIGRlZmF1bHRzIC0gVGhlIGxpc3Qgb2YgZGVmYXVsdCBzaG9ydGN1dHMuXG4gICAqXG4gICAqIEBwYXJhbSB1c2VyIC0gVGhlIGxpc3Qgb2YgdXNlciBzaG9ydGN1dCBvdmVycmlkZXMgYW5kIGFkZGl0aW9ucy5cbiAgICpcbiAgICogQHJldHVybnMgQSBsb2FkYWJsZSBsaXN0IG9mIHNob3J0Y3V0cyAob21pdHRpbmcgZGlzYWJsZWQgYW5kIG92ZXJyaWRkZW4pLlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIHJlY29uY2lsZVNob3J0Y3V0cyhcbiAgICBkZWZhdWx0czogSVNldHRpbmdSZWdpc3RyeS5JU2hvcnRjdXRbXSxcbiAgICB1c2VyOiBJU2V0dGluZ1JlZ2lzdHJ5LklTaG9ydGN1dFtdXG4gICk6IElTZXR0aW5nUmVnaXN0cnkuSVNob3J0Y3V0W10ge1xuICAgIGNvbnN0IG1lbW86IHtcbiAgICAgIFtrZXlzOiBzdHJpbmddOiB7XG4gICAgICAgIFtzZWxlY3Rvcjogc3RyaW5nXTogYm9vbGVhbjsgLy8gSWYgYHRydWVgLCBzaG91bGQgd2FybiBpZiBhIGRlZmF1bHQgc2hvcnRjdXQgY29uZmxpY3RzLlxuICAgICAgfTtcbiAgICB9ID0ge307XG5cbiAgICAvLyBJZiBhIHVzZXIgc2hvcnRjdXQgY29sbGlkZXMgd2l0aCBhbm90aGVyIHVzZXIgc2hvcnRjdXQgd2FybiBhbmQgZmlsdGVyLlxuICAgIHVzZXIgPSB1c2VyLmZpbHRlcihzaG9ydGN1dCA9PiB7XG4gICAgICBjb25zdCBrZXlzID1cbiAgICAgICAgQ29tbWFuZFJlZ2lzdHJ5Lm5vcm1hbGl6ZUtleXMoc2hvcnRjdXQpLmpvaW4oUkVDT1JEX1NFUEFSQVRPUik7XG4gICAgICBpZiAoIWtleXMpIHtcbiAgICAgICAgY29uc29sZS53YXJuKFxuICAgICAgICAgICdTa2lwcGluZyB0aGlzIHNob3J0Y3V0IGJlY2F1c2UgdGhlcmUgYXJlIG5vIGFjdGlvbmFibGUga2V5cyBvbiB0aGlzIHBsYXRmb3JtJyxcbiAgICAgICAgICBzaG9ydGN1dFxuICAgICAgICApO1xuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICB9XG4gICAgICBpZiAoIShrZXlzIGluIG1lbW8pKSB7XG4gICAgICAgIG1lbW9ba2V5c10gPSB7fTtcbiAgICAgIH1cblxuICAgICAgY29uc3QgeyBzZWxlY3RvciB9ID0gc2hvcnRjdXQ7XG4gICAgICBpZiAoIShzZWxlY3RvciBpbiBtZW1vW2tleXNdKSkge1xuICAgICAgICBtZW1vW2tleXNdW3NlbGVjdG9yXSA9IGZhbHNlOyAvLyBEbyBub3Qgd2FybiBpZiBhIGRlZmF1bHQgc2hvcnRjdXQgY29uZmxpY3RzLlxuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICAgIH1cblxuICAgICAgY29uc29sZS53YXJuKFxuICAgICAgICAnU2tpcHBpbmcgdGhpcyBzaG9ydGN1dCBiZWNhdXNlIGl0IGNvbGxpZGVzIHdpdGggYW5vdGhlciBzaG9ydGN1dC4nLFxuICAgICAgICBzaG9ydGN1dFxuICAgICAgKTtcbiAgICAgIHJldHVybiBmYWxzZTtcbiAgICB9KTtcblxuICAgIC8vIElmIGEgZGVmYXVsdCBzaG9ydGN1dCBjb2xsaWRlcyB3aXRoIGFub3RoZXIgZGVmYXVsdCwgd2FybiBhbmQgZmlsdGVyLFxuICAgIC8vIHVubGVzcyBvbmUgb2YgdGhlIHNob3J0Y3V0cyBpcyBhIGRpc2FibGluZyBzaG9ydGN1dCAoc28gbG9vayB0aHJvdWdoXG4gICAgLy8gZGlzYWJsZWQgc2hvcnRjdXRzIGZpcnN0KS4gSWYgYSBzaG9ydGN1dCBoYXMgYWxyZWFkeSBiZWVuIGFkZGVkIGJ5IHRoZVxuICAgIC8vIHVzZXIgcHJlZmVyZW5jZXMsIGZpbHRlciBpdCBvdXQgdG9vICh0aGlzIGluY2x1ZGVzIHNob3J0Y3V0cyB0aGF0IGFyZVxuICAgIC8vIGRpc2FibGVkIGJ5IHVzZXIgcHJlZmVyZW5jZXMpLlxuICAgIGRlZmF1bHRzID0gW1xuICAgICAgLi4uZGVmYXVsdHMuZmlsdGVyKHMgPT4gISFzLmRpc2FibGVkKSxcbiAgICAgIC4uLmRlZmF1bHRzLmZpbHRlcihzID0+ICFzLmRpc2FibGVkKVxuICAgIF0uZmlsdGVyKHNob3J0Y3V0ID0+IHtcbiAgICAgIGNvbnN0IGtleXMgPVxuICAgICAgICBDb21tYW5kUmVnaXN0cnkubm9ybWFsaXplS2V5cyhzaG9ydGN1dCkuam9pbihSRUNPUkRfU0VQQVJBVE9SKTtcblxuICAgICAgaWYgKCFrZXlzKSB7XG4gICAgICAgIHJldHVybiBmYWxzZTtcbiAgICAgIH1cbiAgICAgIGlmICghKGtleXMgaW4gbWVtbykpIHtcbiAgICAgICAgbWVtb1trZXlzXSA9IHt9O1xuICAgICAgfVxuXG4gICAgICBjb25zdCB7IGRpc2FibGVkLCBzZWxlY3RvciB9ID0gc2hvcnRjdXQ7XG4gICAgICBpZiAoIShzZWxlY3RvciBpbiBtZW1vW2tleXNdKSkge1xuICAgICAgICAvLyBXYXJuIG9mIGZ1dHVyZSBjb25mbGljdHMgaWYgdGhlIGRlZmF1bHQgc2hvcnRjdXQgaXMgbm90IGRpc2FibGVkLlxuICAgICAgICBtZW1vW2tleXNdW3NlbGVjdG9yXSA9ICFkaXNhYmxlZDtcbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgICB9XG5cbiAgICAgIC8vIFdlIGhhdmUgYSBjb25mbGljdCBub3cuIFdhcm4gdGhlIHVzZXIgaWYgd2UgbmVlZCB0byBkbyBzby5cbiAgICAgIGlmIChtZW1vW2tleXNdW3NlbGVjdG9yXSkge1xuICAgICAgICBjb25zb2xlLndhcm4oXG4gICAgICAgICAgJ1NraXBwaW5nIHRoaXMgZGVmYXVsdCBzaG9ydGN1dCBiZWNhdXNlIGl0IGNvbGxpZGVzIHdpdGggYW5vdGhlciBkZWZhdWx0IHNob3J0Y3V0LicsXG4gICAgICAgICAgc2hvcnRjdXRcbiAgICAgICAgKTtcbiAgICAgIH1cblxuICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH0pO1xuXG4gICAgLy8gUmV0dXJuIGFsbCB0aGUgc2hvcnRjdXRzIHRoYXQgc2hvdWxkIGJlIHJlZ2lzdGVyZWRcbiAgICByZXR1cm4gKFxuICAgICAgdXNlclxuICAgICAgICAuY29uY2F0KGRlZmF1bHRzKVxuICAgICAgICAuZmlsdGVyKHNob3J0Y3V0ID0+ICFzaG9ydGN1dC5kaXNhYmxlZClcbiAgICAgICAgLy8gRml4IHNob3J0Y3V0cyBjb21wYXJpc29uIGluIHJqc2YgRm9ybSB0byBhdm9pZCBwb2xsdXRpbmcgdGhlIHVzZXIgc2V0dGluZ3NcbiAgICAgICAgLm1hcChzaG9ydGN1dCA9PiB7XG4gICAgICAgICAgcmV0dXJuIHsgYXJnczoge30sIC4uLnNob3J0Y3V0IH07XG4gICAgICAgIH0pXG4gICAgKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBNZXJnZSB0d28gc2V0IG9mIHRvb2xiYXIgaXRlbXMuXG4gICAqXG4gICAqIEBwYXJhbSByZWZlcmVuY2UgUmVmZXJlbmNlIHNldCBvZiB0b29sYmFyIGl0ZW1zXG4gICAqIEBwYXJhbSBhZGRpdGlvbiBOZXcgaXRlbXMgdG8gYWRkXG4gICAqIEBwYXJhbSB3YXJuIFdoZXRoZXIgdG8gd2FybiBpZiBpdGVtIGlzIGR1cGxpY2F0ZWQ7IGRlZmF1bHQgdG8gZmFsc2VcbiAgICogQHJldHVybnMgVGhlIG1lcmdlZCBzZXQgb2YgaXRlbXNcbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiByZWNvbmNpbGVUb29sYmFySXRlbXMoXG4gICAgcmVmZXJlbmNlPzogSVNldHRpbmdSZWdpc3RyeS5JVG9vbGJhckl0ZW1bXSxcbiAgICBhZGRpdGlvbj86IElTZXR0aW5nUmVnaXN0cnkuSVRvb2xiYXJJdGVtW10sXG4gICAgd2FybjogYm9vbGVhbiA9IGZhbHNlXG4gICk6IElTZXR0aW5nUmVnaXN0cnkuSVRvb2xiYXJJdGVtW10gfCB1bmRlZmluZWQge1xuICAgIGlmICghcmVmZXJlbmNlKSB7XG4gICAgICByZXR1cm4gYWRkaXRpb24gPyBKU09ORXh0LmRlZXBDb3B5KGFkZGl0aW9uKSA6IHVuZGVmaW5lZDtcbiAgICB9XG4gICAgaWYgKCFhZGRpdGlvbikge1xuICAgICAgcmV0dXJuIEpTT05FeHQuZGVlcENvcHkocmVmZXJlbmNlKTtcbiAgICB9XG5cbiAgICBjb25zdCBpdGVtcyA9IEpTT05FeHQuZGVlcENvcHkocmVmZXJlbmNlKTtcblxuICAgIC8vIE1lcmdlIGFycmF5IGVsZW1lbnQgZGVwZW5kaW5nIG9uIHRoZSB0eXBlXG4gICAgYWRkaXRpb24uZm9yRWFjaChpdGVtID0+IHtcbiAgICAgIC8vIE5hbWUgbXVzdCBiZSB1bmlxdWUgc28gaXQncyBzdWZmaWNpZW50IHRvIG9ubHkgY29tcGFyZSBpdFxuICAgICAgY29uc3QgcmVmSW5kZXggPSBpdGVtcy5maW5kSW5kZXgocmVmID0+IHJlZi5uYW1lID09PSBpdGVtLm5hbWUpO1xuICAgICAgaWYgKHJlZkluZGV4IDwgMCkge1xuICAgICAgICBpdGVtcy5wdXNoKHsgLi4uaXRlbSB9KTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIGlmIChcbiAgICAgICAgICB3YXJuICYmXG4gICAgICAgICAgSlNPTkV4dC5kZWVwRXF1YWwoT2JqZWN0LmtleXMoaXRlbSksIE9iamVjdC5rZXlzKGl0ZW1zW3JlZkluZGV4XSkpXG4gICAgICAgICkge1xuICAgICAgICAgIGNvbnNvbGUud2FybihgVG9vbGJhciBpdGVtICcke2l0ZW0ubmFtZX0nIGlzIGR1cGxpY2F0ZWQuYCk7XG4gICAgICAgIH1cbiAgICAgICAgaXRlbXNbcmVmSW5kZXhdID0geyAuLi5pdGVtc1tyZWZJbmRleF0sIC4uLml0ZW0gfTtcbiAgICAgIH1cbiAgICB9KTtcblxuICAgIHJldHVybiBpdGVtcztcbiAgfVxufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBgU2V0dGluZ3NgIHN0YXRpY3MuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgU2V0dGluZ3Mge1xuICAvKipcbiAgICogVGhlIGluc3RhbnRpYXRpb24gb3B0aW9ucyBmb3IgYSBgU2V0dGluZ3NgIG9iamVjdC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSU9wdGlvbnMge1xuICAgIC8qKlxuICAgICAqIFRoZSBzZXR0aW5nIHZhbHVlcyBmb3IgYSBwbHVnaW4uXG4gICAgICovXG4gICAgcGx1Z2luOiBJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW47XG5cbiAgICAvKipcbiAgICAgKiBUaGUgc3lzdGVtIHJlZ2lzdHJ5IGluc3RhbmNlIHVzZWQgYnkgdGhlIHNldHRpbmdzIG1hbmFnZXIuXG4gICAgICovXG4gICAgcmVnaXN0cnk6IElTZXR0aW5nUmVnaXN0cnk7XG4gIH1cbn1cblxuLyoqXG4gKiBBIG5hbWVzcGFjZSBmb3IgcHJpdmF0ZSBtb2R1bGUgZGF0YS5cbiAqL1xubmFtZXNwYWNlIFByaXZhdGUge1xuICAvKipcbiAgICogVGhlIGRlZmF1bHQgaW5kZW50YXRpb24gbGV2ZWwsIHVzZXMgc3BhY2VzIGluc3RlYWQgb2YgdGFicy5cbiAgICovXG4gIGNvbnN0IGluZGVudCA9ICcgICAgJztcblxuICAvKipcbiAgICogUmVwbGFjZW1lbnQgdGV4dCBmb3Igc2NoZW1hIHByb3BlcnRpZXMgbWlzc2luZyBhIGBkZXNjcmlwdGlvbmAgZmllbGQuXG4gICAqL1xuICBjb25zdCBub25kZXNjcmlwdCA9ICdbbWlzc2luZyBzY2hlbWEgZGVzY3JpcHRpb25dJztcblxuICAvKipcbiAgICogUmVwbGFjZW1lbnQgdGV4dCBmb3Igc2NoZW1hIHByb3BlcnRpZXMgbWlzc2luZyBhIGB0aXRsZWAgZmllbGQuXG4gICAqL1xuICBjb25zdCB1bnRpdGxlZCA9ICdbbWlzc2luZyBzY2hlbWEgdGl0bGVdJztcblxuICAvKipcbiAgICogUmV0dXJucyBhbiBhbm5vdGF0ZWQgKEpTT04gd2l0aCBjb21tZW50cykgdmVyc2lvbiBvZiBhIHNjaGVtYSdzIGRlZmF1bHRzLlxuICAgKi9cbiAgZXhwb3J0IGZ1bmN0aW9uIGFubm90YXRlZERlZmF1bHRzKFxuICAgIHNjaGVtYTogSVNldHRpbmdSZWdpc3RyeS5JU2NoZW1hLFxuICAgIHBsdWdpbjogc3RyaW5nXG4gICk6IHN0cmluZyB7XG4gICAgY29uc3QgeyBkZXNjcmlwdGlvbiwgcHJvcGVydGllcywgdGl0bGUgfSA9IHNjaGVtYTtcbiAgICBjb25zdCBrZXlzID0gcHJvcGVydGllc1xuICAgICAgPyBPYmplY3Qua2V5cyhwcm9wZXJ0aWVzKS5zb3J0KChhLCBiKSA9PiBhLmxvY2FsZUNvbXBhcmUoYikpXG4gICAgICA6IFtdO1xuICAgIGNvbnN0IGxlbmd0aCA9IE1hdGgubWF4KChkZXNjcmlwdGlvbiB8fCBub25kZXNjcmlwdCkubGVuZ3RoLCBwbHVnaW4ubGVuZ3RoKTtcblxuICAgIHJldHVybiBbXG4gICAgICAneycsXG4gICAgICBwcmVmaXgoYCR7dGl0bGUgfHwgdW50aXRsZWR9YCksXG4gICAgICBwcmVmaXgocGx1Z2luKSxcbiAgICAgIHByZWZpeChkZXNjcmlwdGlvbiB8fCBub25kZXNjcmlwdCksXG4gICAgICBwcmVmaXgoJyonLnJlcGVhdChsZW5ndGgpKSxcbiAgICAgICcnLFxuICAgICAgam9pbihrZXlzLm1hcChrZXkgPT4gZGVmYXVsdERvY3VtZW50ZWRWYWx1ZShzY2hlbWEsIGtleSkpKSxcbiAgICAgICd9J1xuICAgIF0uam9pbignXFxuJyk7XG4gIH1cblxuICAvKipcbiAgICogUmV0dXJucyBhbiBhbm5vdGF0ZWQgKEpTT04gd2l0aCBjb21tZW50cykgdmVyc2lvbiBvZiBhIHBsdWdpbidzXG4gICAqIHNldHRpbmcgZGF0YS5cbiAgICovXG4gIGV4cG9ydCBmdW5jdGlvbiBhbm5vdGF0ZWRQbHVnaW4oXG4gICAgcGx1Z2luOiBJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW4sXG4gICAgZGF0YTogSlNPTk9iamVjdFxuICApOiBzdHJpbmcge1xuICAgIGNvbnN0IHsgZGVzY3JpcHRpb24sIHRpdGxlIH0gPSBwbHVnaW4uc2NoZW1hO1xuICAgIGNvbnN0IGtleXMgPSBPYmplY3Qua2V5cyhkYXRhKS5zb3J0KChhLCBiKSA9PiBhLmxvY2FsZUNvbXBhcmUoYikpO1xuICAgIGNvbnN0IGxlbmd0aCA9IE1hdGgubWF4KFxuICAgICAgKGRlc2NyaXB0aW9uIHx8IG5vbmRlc2NyaXB0KS5sZW5ndGgsXG4gICAgICBwbHVnaW4uaWQubGVuZ3RoXG4gICAgKTtcblxuICAgIHJldHVybiBbXG4gICAgICAneycsXG4gICAgICBwcmVmaXgoYCR7dGl0bGUgfHwgdW50aXRsZWR9YCksXG4gICAgICBwcmVmaXgocGx1Z2luLmlkKSxcbiAgICAgIHByZWZpeChkZXNjcmlwdGlvbiB8fCBub25kZXNjcmlwdCksXG4gICAgICBwcmVmaXgoJyonLnJlcGVhdChsZW5ndGgpKSxcbiAgICAgICcnLFxuICAgICAgam9pbihrZXlzLm1hcChrZXkgPT4gZG9jdW1lbnRlZFZhbHVlKHBsdWdpbi5zY2hlbWEsIGtleSwgZGF0YVtrZXldKSkpLFxuICAgICAgJ30nXG4gICAgXS5qb2luKCdcXG4nKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXR1cm5zIHRoZSBkZWZhdWx0IHZhbHVlLXdpdGgtZG9jdW1lbnRhdGlvbi1zdHJpbmcgZm9yIGFcbiAgICogc3BlY2lmaWMgc2NoZW1hIHByb3BlcnR5LlxuICAgKi9cbiAgZnVuY3Rpb24gZGVmYXVsdERvY3VtZW50ZWRWYWx1ZShcbiAgICBzY2hlbWE6IElTZXR0aW5nUmVnaXN0cnkuSVNjaGVtYSxcbiAgICBrZXk6IHN0cmluZ1xuICApOiBzdHJpbmcge1xuICAgIGNvbnN0IHByb3BzID0gKHNjaGVtYS5wcm9wZXJ0aWVzICYmIHNjaGVtYS5wcm9wZXJ0aWVzW2tleV0pIHx8IHt9O1xuICAgIGNvbnN0IHR5cGUgPSBwcm9wc1sndHlwZSddO1xuICAgIGNvbnN0IGRlc2NyaXB0aW9uID0gcHJvcHNbJ2Rlc2NyaXB0aW9uJ10gfHwgbm9uZGVzY3JpcHQ7XG4gICAgY29uc3QgdGl0bGUgPSBwcm9wc1sndGl0bGUnXSB8fCAnJztcbiAgICBjb25zdCByZWlmaWVkID0gcmVpZnlEZWZhdWx0KHNjaGVtYSwga2V5KTtcbiAgICBjb25zdCBzcGFjZXMgPSBpbmRlbnQubGVuZ3RoO1xuICAgIGNvbnN0IGRlZmF1bHRzID1cbiAgICAgIHJlaWZpZWQgIT09IHVuZGVmaW5lZFxuICAgICAgICA/IHByZWZpeChgXCIke2tleX1cIjogJHtKU09OLnN0cmluZ2lmeShyZWlmaWVkLCBudWxsLCBzcGFjZXMpfWAsIGluZGVudClcbiAgICAgICAgOiBwcmVmaXgoYFwiJHtrZXl9XCI6ICR7dHlwZX1gKTtcblxuICAgIHJldHVybiBbcHJlZml4KHRpdGxlKSwgcHJlZml4KGRlc2NyaXB0aW9uKSwgZGVmYXVsdHNdXG4gICAgICAuZmlsdGVyKHN0ciA9PiBzdHIubGVuZ3RoKVxuICAgICAgLmpvaW4oJ1xcbicpO1xuICB9XG5cbiAgLyoqXG4gICAqIFJldHVybnMgYSB2YWx1ZS13aXRoLWRvY3VtZW50YXRpb24tc3RyaW5nIGZvciBhIHNwZWNpZmljIHNjaGVtYSBwcm9wZXJ0eS5cbiAgICovXG4gIGZ1bmN0aW9uIGRvY3VtZW50ZWRWYWx1ZShcbiAgICBzY2hlbWE6IElTZXR0aW5nUmVnaXN0cnkuSVNjaGVtYSxcbiAgICBrZXk6IHN0cmluZyxcbiAgICB2YWx1ZTogSlNPTlZhbHVlXG4gICk6IHN0cmluZyB7XG4gICAgY29uc3QgcHJvcHMgPSBzY2hlbWEucHJvcGVydGllcyAmJiBzY2hlbWEucHJvcGVydGllc1trZXldO1xuICAgIGNvbnN0IGRlc2NyaXB0aW9uID0gKHByb3BzICYmIHByb3BzWydkZXNjcmlwdGlvbiddKSB8fCBub25kZXNjcmlwdDtcbiAgICBjb25zdCB0aXRsZSA9IChwcm9wcyAmJiBwcm9wc1sndGl0bGUnXSkgfHwgdW50aXRsZWQ7XG4gICAgY29uc3Qgc3BhY2VzID0gaW5kZW50Lmxlbmd0aDtcbiAgICBjb25zdCBhdHRyaWJ1dGUgPSBwcmVmaXgoXG4gICAgICBgXCIke2tleX1cIjogJHtKU09OLnN0cmluZ2lmeSh2YWx1ZSwgbnVsbCwgc3BhY2VzKX1gLFxuICAgICAgaW5kZW50XG4gICAgKTtcblxuICAgIHJldHVybiBbcHJlZml4KHRpdGxlKSwgcHJlZml4KGRlc2NyaXB0aW9uKSwgYXR0cmlidXRlXS5qb2luKCdcXG4nKTtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZXR1cm5zIGEgam9pbmVkIHN0cmluZyB3aXRoIGxpbmUgYnJlYWtzIGFuZCBjb21tYXMgd2hlcmUgYXBwcm9wcmlhdGUuXG4gICAqL1xuICBmdW5jdGlvbiBqb2luKGJvZHk6IHN0cmluZ1tdKTogc3RyaW5nIHtcbiAgICByZXR1cm4gYm9keS5yZWR1Y2UoKGFjYywgdmFsLCBpZHgpID0+IHtcbiAgICAgIGNvbnN0IHJvd3MgPSB2YWwuc3BsaXQoJ1xcbicpO1xuICAgICAgY29uc3QgbGFzdCA9IHJvd3Nbcm93cy5sZW5ndGggLSAxXTtcbiAgICAgIGNvbnN0IGNvbW1lbnQgPSBsYXN0LnRyaW0oKS5pbmRleE9mKCcvLycpID09PSAwO1xuICAgICAgY29uc3QgY29tbWEgPSBjb21tZW50IHx8IGlkeCA9PT0gYm9keS5sZW5ndGggLSAxID8gJycgOiAnLCc7XG4gICAgICBjb25zdCBzZXBhcmF0b3IgPSBpZHggPT09IGJvZHkubGVuZ3RoIC0gMSA/ICcnIDogJ1xcblxcbic7XG5cbiAgICAgIHJldHVybiBhY2MgKyB2YWwgKyBjb21tYSArIHNlcGFyYXRvcjtcbiAgICB9LCAnJyk7XG4gIH1cblxuICAvKipcbiAgICogUmV0dXJucyBhIGRvY3VtZW50YXRpb24gc3RyaW5nIHdpdGggYSBjb21tZW50IHByZWZpeCBhZGRlZCBvbiBldmVyeSBsaW5lLlxuICAgKi9cbiAgZnVuY3Rpb24gcHJlZml4KHNvdXJjZTogc3RyaW5nLCBwcmUgPSBgJHtpbmRlbnR9Ly8gYCk6IHN0cmluZyB7XG4gICAgcmV0dXJuIHByZSArIHNvdXJjZS5zcGxpdCgnXFxuJykuam9pbihgXFxuJHtwcmV9YCk7XG4gIH1cblxuICAvKipcbiAgICogQ3JlYXRlIGEgZnVsbHkgZXh0cmFwb2xhdGVkIGRlZmF1bHQgdmFsdWUgZm9yIGEgcm9vdCBrZXkgaW4gYSBzY2hlbWEuXG4gICAqL1xuICBleHBvcnQgZnVuY3Rpb24gcmVpZnlEZWZhdWx0KFxuICAgIHNjaGVtYTogSVNldHRpbmdSZWdpc3RyeS5JUHJvcGVydHksXG4gICAgcm9vdD86IHN0cmluZ1xuICApOiBQYXJ0aWFsSlNPTlZhbHVlIHwgdW5kZWZpbmVkIHtcbiAgICBjb25zdCBkZWZpbml0aW9ucyA9IHNjaGVtYS5kZWZpbml0aW9ucyBhcyBQYXJ0aWFsSlNPTk9iamVjdDtcbiAgICAvLyBJZiB0aGUgcHJvcGVydHkgaXMgYXQgdGhlIHJvb3QgbGV2ZWwsIHRyYXZlcnNlIGl0cyBzY2hlbWEuXG4gICAgc2NoZW1hID0gKHJvb3QgPyBzY2hlbWEucHJvcGVydGllcz8uW3Jvb3RdIDogc2NoZW1hKSB8fCB7fTtcblxuICAgIGlmIChzY2hlbWEudHlwZSA9PT0gJ29iamVjdCcpIHtcbiAgICAgIC8vIE1ha2UgYSBjb3B5IG9mIHRoZSBkZWZhdWx0IHZhbHVlIHRvIHBvcHVsYXRlLlxuICAgICAgY29uc3QgcmVzdWx0ID0gSlNPTkV4dC5kZWVwQ29weShzY2hlbWEuZGVmYXVsdCBhcyBQYXJ0aWFsSlNPTk9iamVjdCk7XG5cbiAgICAgIC8vIEl0ZXJhdGUgdGhyb3VnaCBhbmQgcG9wdWxhdGUgZWFjaCBjaGlsZCBwcm9wZXJ0eS5cbiAgICAgIGNvbnN0IHByb3BzID0gc2NoZW1hLnByb3BlcnRpZXMgfHwge307XG4gICAgICBmb3IgKGNvbnN0IHByb3BlcnR5IGluIHByb3BzKSB7XG4gICAgICAgIHJlc3VsdFtwcm9wZXJ0eV0gPSByZWlmeURlZmF1bHQocHJvcHNbcHJvcGVydHldKTtcbiAgICAgIH1cblxuICAgICAgcmV0dXJuIHJlc3VsdDtcbiAgICB9IGVsc2UgaWYgKHNjaGVtYS50eXBlID09PSAnYXJyYXknKSB7XG4gICAgICAvLyBNYWtlIGEgY29weSBvZiB0aGUgZGVmYXVsdCB2YWx1ZSB0byBwb3B1bGF0ZS5cbiAgICAgIGNvbnN0IHJlc3VsdCA9IEpTT05FeHQuZGVlcENvcHkoc2NoZW1hLmRlZmF1bHQgYXMgUGFydGlhbEpTT05BcnJheSk7XG5cbiAgICAgIC8vIEl0ZW1zIGRlZmluZXMgdGhlIHByb3BlcnRpZXMgb2YgZWFjaCBpdGVtIGluIHRoZSBhcnJheVxuICAgICAgbGV0IHByb3BzID0gKHNjaGVtYS5pdGVtcyBhcyBQYXJ0aWFsSlNPTk9iamVjdCkgfHwge307XG4gICAgICAvLyBVc2UgcmVmZXJlbmNlZCBkZWZpbml0aW9uIGlmIG9uZSBleGlzdHNcbiAgICAgIGlmIChwcm9wc1snJHJlZiddICYmIGRlZmluaXRpb25zKSB7XG4gICAgICAgIGNvbnN0IHJlZjogc3RyaW5nID0gKHByb3BzWyckcmVmJ10gYXMgc3RyaW5nKS5yZXBsYWNlKFxuICAgICAgICAgICcjL2RlZmluaXRpb25zLycsXG4gICAgICAgICAgJydcbiAgICAgICAgKTtcbiAgICAgICAgcHJvcHMgPSAoZGVmaW5pdGlvbnNbcmVmXSBhcyBQYXJ0aWFsSlNPTk9iamVjdCkgPz8ge307XG4gICAgICB9XG4gICAgICAvLyBJdGVyYXRlIHRocm91Z2ggdGhlIGl0ZW1zIGluIHRoZSBhcnJheSBhbmQgZmlsbCBpbiBkZWZhdWx0c1xuICAgICAgZm9yIChjb25zdCBpdGVtIGluIHJlc3VsdCkge1xuICAgICAgICAvLyBVc2UgdGhlIHZhbHVlcyB0aGF0IGFyZSBoYXJkLWNvZGVkIGluIHRoZSBkZWZhdWx0IGFycmF5IG92ZXIgdGhlIGRlZmF1bHRzIGZvciBlYWNoIGZpZWxkLlxuICAgICAgICBjb25zdCByZWlmaWVkID0gKHJlaWZ5RGVmYXVsdChwcm9wcykgYXMgUGFydGlhbEpTT05PYmplY3QpIHx8IHt9O1xuICAgICAgICBmb3IgKGNvbnN0IHByb3AgaW4gcmVpZmllZCkge1xuICAgICAgICAgIGlmICgocmVzdWx0W2l0ZW1dIGFzIFBhcnRpYWxKU09OT2JqZWN0KT8uW3Byb3BdKSB7XG4gICAgICAgICAgICByZWlmaWVkW3Byb3BdID0gKHJlc3VsdFtpdGVtXSBhcyBQYXJ0aWFsSlNPTk9iamVjdClbcHJvcF07XG4gICAgICAgICAgfVxuICAgICAgICB9XG4gICAgICAgIHJlc3VsdFtpdGVtXSA9IHJlaWZpZWQ7XG4gICAgICB9XG5cbiAgICAgIHJldHVybiByZXN1bHQ7XG4gICAgfSBlbHNlIHtcbiAgICAgIHJldHVybiBzY2hlbWEuZGVmYXVsdDtcbiAgICB9XG4gIH1cbn1cbiIsIi8qIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG58IENvcHlyaWdodCAoYykgSnVweXRlciBEZXZlbG9wbWVudCBUZWFtLlxufCBEaXN0cmlidXRlZCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIE1vZGlmaWVkIEJTRCBMaWNlbnNlLlxufC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qL1xuXG5pbXBvcnQgeyBJRGF0YUNvbm5lY3RvciB9IGZyb20gJ0BqdXB5dGVybGFiL3N0YXRlZGInO1xuaW1wb3J0IHtcbiAgUGFydGlhbEpTT05PYmplY3QsXG4gIFBhcnRpYWxKU09OVmFsdWUsXG4gIFJlYWRvbmx5UGFydGlhbEpTT05PYmplY3QsXG4gIFJlYWRvbmx5UGFydGlhbEpTT05WYWx1ZSxcbiAgVG9rZW5cbn0gZnJvbSAnQGx1bWluby9jb3JldXRpbHMnO1xuaW1wb3J0IHsgSURpc3Bvc2FibGUgfSBmcm9tICdAbHVtaW5vL2Rpc3Bvc2FibGUnO1xuaW1wb3J0IHsgSVNpZ25hbCB9IGZyb20gJ0BsdW1pbm8vc2lnbmFsaW5nJztcbmltcG9ydCB7IElTY2hlbWFWYWxpZGF0b3IgfSBmcm9tICcuL3NldHRpbmdyZWdpc3RyeSc7XG5cbi8qKlxuICogVGhlIHNldHRpbmcgcmVnaXN0cnkgdG9rZW4uXG4gKi9cbmV4cG9ydCBjb25zdCBJU2V0dGluZ1JlZ2lzdHJ5ID0gbmV3IFRva2VuPElTZXR0aW5nUmVnaXN0cnk+KFxuICAnQGp1cHl0ZXJsYWIvY29yZXV0aWxzOklTZXR0aW5nUmVnaXN0cnknXG4pO1xuXG4vKipcbiAqIFRoZSBzZXR0aW5ncyByZWdpc3RyeSBpbnRlcmZhY2UuXG4gKi9cbmV4cG9ydCBpbnRlcmZhY2UgSVNldHRpbmdSZWdpc3RyeSB7XG4gIC8qKlxuICAgKiBUaGUgZGF0YSBjb25uZWN0b3IgdXNlZCBieSB0aGUgc2V0dGluZyByZWdpc3RyeS5cbiAgICovXG4gIHJlYWRvbmx5IGNvbm5lY3RvcjogSURhdGFDb25uZWN0b3I8SVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luLCBzdHJpbmcsIHN0cmluZz47XG5cbiAgLyoqXG4gICAqIFRoZSBzY2hlbWEgb2YgdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAqL1xuICByZWFkb25seSBzY2hlbWE6IElTZXR0aW5nUmVnaXN0cnkuSVNjaGVtYTtcblxuICAvKipcbiAgICogVGhlIHNjaGVtYSB2YWxpZGF0b3IgdXNlZCBieSB0aGUgc2V0dGluZyByZWdpc3RyeS5cbiAgICovXG4gIHJlYWRvbmx5IHZhbGlkYXRvcjogSVNjaGVtYVZhbGlkYXRvcjtcblxuICAvKipcbiAgICogQSBzaWduYWwgdGhhdCBlbWl0cyB0aGUgbmFtZSBvZiBhIHBsdWdpbiB3aGVuIGl0cyBzZXR0aW5ncyBjaGFuZ2UuXG4gICAqL1xuICByZWFkb25seSBwbHVnaW5DaGFuZ2VkOiBJU2lnbmFsPHRoaXMsIHN0cmluZz47XG5cbiAgLyoqXG4gICAqIFRoZSBjb2xsZWN0aW9uIG9mIHNldHRpbmcgcmVnaXN0cnkgcGx1Z2lucy5cbiAgICovXG4gIHJlYWRvbmx5IHBsdWdpbnM6IHtcbiAgICBbbmFtZTogc3RyaW5nXTogSVNldHRpbmdSZWdpc3RyeS5JUGx1Z2luIHwgdW5kZWZpbmVkO1xuICB9O1xuXG4gIC8qKlxuICAgKiBHZXQgYW4gaW5kaXZpZHVhbCBzZXR0aW5nLlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIG5hbWUgb2YgdGhlIHBsdWdpbiB3aG9zZSBzZXR0aW5ncyBhcmUgYmVpbmcgcmV0cmlldmVkLlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgcmV0cmlldmVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBzZXR0aW5nIGlzIHJldHJpZXZlZC5cbiAgICovXG4gIGdldChcbiAgICBwbHVnaW46IHN0cmluZyxcbiAgICBrZXk6IHN0cmluZ1xuICApOiBQcm9taXNlPHtcbiAgICBjb21wb3NpdGU6IFBhcnRpYWxKU09OVmFsdWUgfCB1bmRlZmluZWQ7XG4gICAgdXNlcjogUGFydGlhbEpTT05WYWx1ZSB8IHVuZGVmaW5lZDtcbiAgfT47XG5cbiAgLyoqXG4gICAqIExvYWQgYSBwbHVnaW4ncyBzZXR0aW5ncyBpbnRvIHRoZSBzZXR0aW5nIHJlZ2lzdHJ5LlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIG5hbWUgb2YgdGhlIHBsdWdpbiB3aG9zZSBzZXR0aW5ncyBhcmUgYmVpbmcgbG9hZGVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aXRoIGEgcGx1Z2luIHNldHRpbmdzIG9iamVjdCBvciByZWplY3RzXG4gICAqIGlmIHRoZSBwbHVnaW4gaXMgbm90IGZvdW5kLlxuICAgKi9cbiAgbG9hZChwbHVnaW46IHN0cmluZyk6IFByb21pc2U8SVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3M+O1xuXG4gIC8qKlxuICAgKiBSZWxvYWQgYSBwbHVnaW4ncyBzZXR0aW5ncyBpbnRvIHRoZSByZWdpc3RyeSBldmVuIGlmIHRoZXkgYWxyZWFkeSBleGlzdC5cbiAgICpcbiAgICogQHBhcmFtIHBsdWdpbiAtIFRoZSBuYW1lIG9mIHRoZSBwbHVnaW4gd2hvc2Ugc2V0dGluZ3MgYXJlIGJlaW5nIHJlbG9hZGVkLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aXRoIGEgcGx1Z2luIHNldHRpbmdzIG9iamVjdCBvciByZWplY3RzXG4gICAqIHdpdGggYSBsaXN0IG9mIGBJU2NoZW1hVmFsaWRhdG9yLklFcnJvcmAgb2JqZWN0cyBpZiBpdCBmYWlscy5cbiAgICovXG4gIHJlbG9hZChwbHVnaW46IHN0cmluZyk6IFByb21pc2U8SVNldHRpbmdSZWdpc3RyeS5JU2V0dGluZ3M+O1xuXG4gIC8qKlxuICAgKiBSZW1vdmUgYSBzaW5nbGUgc2V0dGluZyBpbiB0aGUgcmVnaXN0cnkuXG4gICAqXG4gICAqIEBwYXJhbSBwbHVnaW4gLSBUaGUgbmFtZSBvZiB0aGUgcGx1Z2luIHdob3NlIHNldHRpbmcgaXMgYmVpbmcgcmVtb3ZlZC5cbiAgICpcbiAgICogQHBhcmFtIGtleSAtIFRoZSBuYW1lIG9mIHRoZSBzZXR0aW5nIGJlaW5nIHJlbW92ZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIHNldHRpbmcgaXMgcmVtb3ZlZC5cbiAgICovXG4gIHJlbW92ZShwbHVnaW46IHN0cmluZywga2V5OiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+O1xuXG4gIC8qKlxuICAgKiBTZXQgYSBzaW5nbGUgc2V0dGluZyBpbiB0aGUgcmVnaXN0cnkuXG4gICAqXG4gICAqIEBwYXJhbSBwbHVnaW4gLSBUaGUgbmFtZSBvZiB0aGUgcGx1Z2luIHdob3NlIHNldHRpbmcgaXMgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcGFyYW0gdmFsdWUgLSBUaGUgdmFsdWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcmV0dXJucyBBIHByb21pc2UgdGhhdCByZXNvbHZlcyB3aGVuIHRoZSBzZXR0aW5nIGhhcyBiZWVuIHNhdmVkLlxuICAgKlxuICAgKi9cbiAgc2V0KHBsdWdpbjogc3RyaW5nLCBrZXk6IHN0cmluZywgdmFsdWU6IFBhcnRpYWxKU09OVmFsdWUpOiBQcm9taXNlPHZvaWQ+O1xuXG4gIC8qKlxuICAgKiBSZWdpc3RlciBhIHBsdWdpbiB0cmFuc2Zvcm0gZnVuY3Rpb24gdG8gYWN0IG9uIGEgc3BlY2lmaWMgcGx1Z2luLlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIG5hbWUgb2YgdGhlIHBsdWdpbiB3aG9zZSBzZXR0aW5ncyBhcmUgdHJhbnNmb3JtZWQuXG4gICAqXG4gICAqIEBwYXJhbSB0cmFuc2Zvcm1zIC0gVGhlIHRyYW5zZm9ybSBmdW5jdGlvbnMgYXBwbGllZCB0byB0aGUgcGx1Z2luLlxuICAgKlxuICAgKiBAcmV0dXJucyBBIGRpc3Bvc2FibGUgdGhhdCByZW1vdmVzIHRoZSB0cmFuc2Zvcm1zIGZyb20gdGhlIHJlZ2lzdHJ5LlxuICAgKlxuICAgKiAjIyMjIE5vdGVzXG4gICAqIC0gYGNvbXBvc2VgIHRyYW5zZm9ybWF0aW9uczogVGhlIHJlZ2lzdHJ5IGF1dG9tYXRpY2FsbHkgb3ZlcndyaXRlcyBhXG4gICAqIHBsdWdpbidzIGRlZmF1bHQgdmFsdWVzIHdpdGggdXNlciBvdmVycmlkZXMsIGJ1dCBhIHBsdWdpbiBtYXkgaW5zdGVhZCB3aXNoXG4gICAqIHRvIG1lcmdlIHZhbHVlcy4gVGhpcyBiZWhhdmlvciBjYW4gYmUgYWNjb21wbGlzaGVkIGluIGEgYGNvbXBvc2VgXG4gICAqIHRyYW5zZm9ybWF0aW9uLlxuICAgKiAtIGBmZXRjaGAgdHJhbnNmb3JtYXRpb25zOiBUaGUgcmVnaXN0cnkgdXNlcyB0aGUgcGx1Z2luIGRhdGEgdGhhdCBpc1xuICAgKiBmZXRjaGVkIGZyb20gaXRzIGNvbm5lY3Rvci4gSWYgYSBwbHVnaW4gd2FudHMgdG8gb3ZlcnJpZGUsIGUuZy4gdG8gdXBkYXRlXG4gICAqIGl0cyBzY2hlbWEgd2l0aCBkeW5hbWljIGRlZmF1bHRzLCBhIGBmZXRjaGAgdHJhbnNmb3JtYXRpb24gY2FuIGJlIGFwcGxpZWQuXG4gICAqL1xuICB0cmFuc2Zvcm0oXG4gICAgcGx1Z2luOiBzdHJpbmcsXG4gICAgdHJhbnNmb3Jtczoge1xuICAgICAgW3BoYXNlIGluIElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbi5QaGFzZV0/OiBJU2V0dGluZ1JlZ2lzdHJ5LklQbHVnaW4uVHJhbnNmb3JtO1xuICAgIH1cbiAgKTogSURpc3Bvc2FibGU7XG5cbiAgLyoqXG4gICAqIFVwbG9hZCBhIHBsdWdpbidzIHNldHRpbmdzLlxuICAgKlxuICAgKiBAcGFyYW0gcGx1Z2luIC0gVGhlIG5hbWUgb2YgdGhlIHBsdWdpbiB3aG9zZSBzZXR0aW5ncyBhcmUgYmVpbmcgc2V0LlxuICAgKlxuICAgKiBAcGFyYW0gcmF3IC0gVGhlIHJhdyBwbHVnaW4gc2V0dGluZ3MgYmVpbmcgdXBsb2FkZWQuXG4gICAqXG4gICAqIEByZXR1cm5zIEEgcHJvbWlzZSB0aGF0IHJlc29sdmVzIHdoZW4gdGhlIHNldHRpbmdzIGhhdmUgYmVlbiBzYXZlZC5cbiAgICovXG4gIHVwbG9hZChwbHVnaW46IHN0cmluZywgcmF3OiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+O1xufVxuXG4vKipcbiAqIEEgbmFtZXNwYWNlIGZvciBzZXR0aW5nIHJlZ2lzdHJ5IGludGVyZmFjZXMuXG4gKi9cbmV4cG9ydCBuYW1lc3BhY2UgSVNldHRpbmdSZWdpc3RyeSB7XG4gIC8qKlxuICAgKiBUaGUgcHJpbWl0aXZlIHR5cGVzIGF2YWlsYWJsZSBpbiBhIEpTT04gc2NoZW1hLlxuICAgKi9cbiAgZXhwb3J0IHR5cGUgUHJpbWl0aXZlID1cbiAgICB8ICdhcnJheSdcbiAgICB8ICdib29sZWFuJ1xuICAgIHwgJ251bGwnXG4gICAgfCAnbnVtYmVyJ1xuICAgIHwgJ29iamVjdCdcbiAgICB8ICdzdHJpbmcnO1xuXG4gIC8qKlxuICAgKiBUaGUgbWVudSBpZHMgZGVmaW5lZCBieSBkZWZhdWx0LlxuICAgKi9cbiAgZXhwb3J0IHR5cGUgRGVmYXVsdE1lbnVJZCA9XG4gICAgfCAnanAtbWVudS1maWxlJ1xuICAgIHwgJ2pwLW1lbnUtZmlsZS1uZXcnXG4gICAgfCAnanAtbWVudS1lZGl0J1xuICAgIHwgJ2pwLW1lbnUtaGVscCdcbiAgICB8ICdqcC1tZW51LWtlcm5lbCdcbiAgICB8ICdqcC1tZW51LXJ1bidcbiAgICB8ICdqcC1tZW51LXNldHRpbmdzJ1xuICAgIHwgJ2pwLW1lbnUtdmlldydcbiAgICB8ICdqcC1tZW51LXRhYnMnO1xuXG4gIC8qKlxuICAgKiBBbiBpbnRlcmZhY2UgZGVmaW5pbmcgYSBtZW51LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJTWVudSBleHRlbmRzIFBhcnRpYWxKU09OT2JqZWN0IHtcbiAgICAvKipcbiAgICAgKiBVbmlxdWUgbWVudSBpZGVudGlmaWVyXG4gICAgICovXG4gICAgaWQ6IERlZmF1bHRNZW51SWQgfCBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBNZW51IGl0ZW1zXG4gICAgICovXG4gICAgaXRlbXM/OiBJTWVudUl0ZW1bXTtcblxuICAgIC8qKlxuICAgICAqIFRoZSByYW5rIG9yZGVyIG9mIHRoZSBtZW51IGFtb25nIGl0cyBzaWJsaW5ncy5cbiAgICAgKi9cbiAgICByYW5rPzogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogTWVudSB0aXRsZVxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIERlZmF1bHQgd2lsbCBiZSB0aGUgY2FwaXRhbGl6ZWQgaWQuXG4gICAgICovXG4gICAgbGFiZWw/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBNZW51IGljb24gaWRcbiAgICAgKlxuICAgICAqICMjIyMgTm90ZVxuICAgICAqIFRoZSBpY29uIGlkIHdpbGwgbG9va2VkIGZvciBpbiByZWdpc3RlcmVkIExhYkljb24uXG4gICAgICovXG4gICAgaWNvbj86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIEdldCB0aGUgbW5lbW9uaWMgaW5kZXggZm9yIHRoZSB0aXRsZS5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGUgZGVmYXVsdCB2YWx1ZSBpcyBgLTFgLlxuICAgICAqL1xuICAgIG1uZW1vbmljPzogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciBhIG1lbnUgaXMgZGlzYWJsZWQuIGBGYWxzZWAgYnkgZGVmYXVsdC5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGlzIGFsbG93cyBhbiB1c2VyIHRvIHN1cHByZXNzIGEgbWVudS5cbiAgICAgKi9cbiAgICBkaXNhYmxlZD86IGJvb2xlYW47XG4gIH1cblxuICAvKipcbiAgICogQW4gaW50ZXJmYWNlIGRlc2NyaWJpbmcgYSBtZW51IGl0ZW0uXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElNZW51SXRlbSBleHRlbmRzIFBhcnRpYWxKU09OT2JqZWN0IHtcbiAgICAvKipcbiAgICAgKiBUaGUgdHlwZSBvZiB0aGUgbWVudSBpdGVtLlxuICAgICAqXG4gICAgICogVGhlIGRlZmF1bHQgdmFsdWUgaXMgYCdjb21tYW5kJ2AuXG4gICAgICovXG4gICAgdHlwZT86ICdjb21tYW5kJyB8ICdzdWJtZW51JyB8ICdzZXBhcmF0b3InO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbW1hbmQgdG8gZXhlY3V0ZSB3aGVuIHRoZSBpdGVtIGlzIHRyaWdnZXJlZC5cbiAgICAgKlxuICAgICAqIFRoZSBkZWZhdWx0IHZhbHVlIGlzIGFuIGVtcHR5IHN0cmluZy5cbiAgICAgKi9cbiAgICBjb21tYW5kPzogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGFyZ3VtZW50cyBmb3IgdGhlIGNvbW1hbmQuXG4gICAgICpcbiAgICAgKiBUaGUgZGVmYXVsdCB2YWx1ZSBpcyBhbiBlbXB0eSBvYmplY3QuXG4gICAgICovXG4gICAgYXJncz86IFBhcnRpYWxKU09OT2JqZWN0O1xuXG4gICAgLyoqXG4gICAgICogVGhlIHJhbmsgb3JkZXIgb2YgdGhlIG1lbnUgaXRlbSBhbW9uZyBpdHMgc2libGluZ3MuXG4gICAgICovXG4gICAgcmFuaz86IG51bWJlcjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBzdWJtZW51IGZvciBhIGAnc3VibWVudSdgIHR5cGUgaXRlbS5cbiAgICAgKlxuICAgICAqIFRoZSBkZWZhdWx0IHZhbHVlIGlzIGBudWxsYC5cbiAgICAgKi9cbiAgICBzdWJtZW51PzogSU1lbnUgfCBudWxsO1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciBhIG1lbnUgaXRlbSBpcyBkaXNhYmxlZC4gYGZhbHNlYCBieSBkZWZhdWx0LlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoaXMgYWxsb3dzIGFuIHVzZXIgdG8gc3VwcHJlc3MgbWVudSBpdGVtcy5cbiAgICAgKi9cbiAgICBkaXNhYmxlZD86IGJvb2xlYW47XG4gIH1cblxuICAvKipcbiAgICogQW4gaW50ZXJmYWNlIGRlc2NyaWJpbmcgYSBjb250ZXh0IG1lbnUgaXRlbVxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJQ29udGV4dE1lbnVJdGVtIGV4dGVuZHMgSU1lbnVJdGVtIHtcbiAgICAvKipcbiAgICAgKiBUaGUgQ1NTIHNlbGVjdG9yIGZvciB0aGUgY29udGV4dCBtZW51IGl0ZW0uXG4gICAgICpcbiAgICAgKiBUaGUgY29udGV4dCBtZW51IGl0ZW0gd2lsbCBvbmx5IGJlIGRpc3BsYXllZCBpbiB0aGUgY29udGV4dCBtZW51XG4gICAgICogd2hlbiB0aGUgc2VsZWN0b3IgbWF0Y2hlcyBhIG5vZGUgb24gdGhlIHByb3BhZ2F0aW9uIHBhdGggb2YgdGhlXG4gICAgICogY29udGV4dG1lbnUgZXZlbnQuIFRoaXMgYWxsb3dzIHRoZSBtZW51IGl0ZW0gdG8gYmUgcmVzdHJpY3RlZCB0b1xuICAgICAqIHVzZXItZGVmaW5lZCBjb250ZXh0cy5cbiAgICAgKlxuICAgICAqIFRoZSBzZWxlY3RvciBtdXN0IG5vdCBjb250YWluIGNvbW1hcy5cbiAgICAgKi9cbiAgICBzZWxlY3Rvcjogc3RyaW5nO1xuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBzZXR0aW5ncyBmb3IgYSBzcGVjaWZpYyBwbHVnaW4uXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElQbHVnaW4gZXh0ZW5kcyBQYXJ0aWFsSlNPTk9iamVjdCB7XG4gICAgLyoqXG4gICAgICogVGhlIG5hbWUgb2YgdGhlIHBsdWdpbi5cbiAgICAgKi9cbiAgICBpZDogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbGxlY3Rpb24gb2YgdmFsdWVzIGZvciBhIHNwZWNpZmllZCBwbHVnaW4uXG4gICAgICovXG4gICAgZGF0YTogSVNldHRpbmdCdW5kbGU7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcmF3IHVzZXIgc2V0dGluZ3MgZGF0YSBhcyBhIHN0cmluZyBjb250YWluaW5nIEpTT04gd2l0aCBjb21tZW50cy5cbiAgICAgKi9cbiAgICByYXc6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBKU09OIHNjaGVtYSBmb3IgdGhlIHBsdWdpbi5cbiAgICAgKi9cbiAgICBzY2hlbWE6IElTY2hlbWE7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcHVibGlzaGVkIHZlcnNpb24gb2YgdGhlIE5QTSBwYWNrYWdlIGNvbnRhaW5pbmcgdGhlIHBsdWdpbi5cbiAgICAgKi9cbiAgICB2ZXJzaW9uOiBzdHJpbmc7XG4gIH1cblxuICAvKipcbiAgICogQSBuYW1lc3BhY2UgZm9yIHBsdWdpbiBmdW5jdGlvbmFsaXR5LlxuICAgKi9cbiAgZXhwb3J0IG5hbWVzcGFjZSBJUGx1Z2luIHtcbiAgICAvKipcbiAgICAgKiBBIGZ1bmN0aW9uIHRoYXQgdHJhbnNmb3JtcyBhIHBsdWdpbiBvYmplY3QgYmVmb3JlIGl0IGlzIGNvbnN1bWVkIGJ5IHRoZVxuICAgICAqIHNldHRpbmcgcmVnaXN0cnkuXG4gICAgICovXG4gICAgZXhwb3J0IHR5cGUgVHJhbnNmb3JtID0gKHBsdWdpbjogSVBsdWdpbikgPT4gSVBsdWdpbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwaGFzZXMgZHVyaW5nIHdoaWNoIGEgdHJhbnNmb3JtYXRpb24gbWF5IGJlIGFwcGxpZWQgdG8gYSBwbHVnaW4uXG4gICAgICovXG4gICAgZXhwb3J0IHR5cGUgUGhhc2UgPSAnY29tcG9zZScgfCAnZmV0Y2gnO1xuICB9XG5cbiAgLyoqXG4gICAqIEEgbWluaW1hbCBzdWJzZXQgb2YgdGhlIGZvcm1hbCBKU09OIFNjaGVtYSB0aGF0IGRlc2NyaWJlcyBhIHByb3BlcnR5LlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJUHJvcGVydHkgZXh0ZW5kcyBQYXJ0aWFsSlNPTk9iamVjdCB7XG4gICAgLyoqXG4gICAgICogVGhlIGRlZmF1bHQgdmFsdWUsIGlmIGFueS5cbiAgICAgKi9cbiAgICBkZWZhdWx0PzogUGFydGlhbEpTT05WYWx1ZTtcblxuICAgIC8qKlxuICAgICAqIFRoZSBzY2hlbWEgZGVzY3JpcHRpb24uXG4gICAgICovXG4gICAgZGVzY3JpcHRpb24/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgc2NoZW1hJ3MgY2hpbGQgcHJvcGVydGllcy5cbiAgICAgKi9cbiAgICBwcm9wZXJ0aWVzPzogeyBbcHJvcGVydHk6IHN0cmluZ106IElQcm9wZXJ0eSB9O1xuXG4gICAgLyoqXG4gICAgICogVGhlIHRpdGxlIG9mIGEgcHJvcGVydHkuXG4gICAgICovXG4gICAgdGl0bGU/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgdHlwZSBvciB0eXBlcyBvZiB0aGUgZGF0YS5cbiAgICAgKi9cbiAgICB0eXBlPzogUHJpbWl0aXZlIHwgUHJpbWl0aXZlW107XG4gIH1cblxuICAvKipcbiAgICogQSBzY2hlbWEgdHlwZSB0aGF0IGlzIGEgbWluaW1hbCBzdWJzZXQgb2YgdGhlIGZvcm1hbCBKU09OIFNjaGVtYSBhbG9uZyB3aXRoXG4gICAqIG9wdGlvbmFsIEp1cHl0ZXJMYWIgcmVuZGVyaW5nIGhpbnRzLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJU2NoZW1hIGV4dGVuZHMgSVByb3BlcnR5IHtcbiAgICAvKipcbiAgICAgKiBUaGUgSnVweXRlckxhYiBtZW51cyB0aGF0IGFyZSBjcmVhdGVkIGJ5IGEgcGx1Z2luJ3Mgc2NoZW1hLlxuICAgICAqL1xuICAgICdqdXB5dGVyLmxhYi5tZW51cyc/OiB7XG4gICAgICBtYWluOiBJTWVudVtdO1xuICAgICAgY29udGV4dDogSUNvbnRleHRNZW51SXRlbVtdO1xuICAgIH07XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIHRoZSBzY2hlbWEgaXMgZGVwcmVjYXRlZC5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGlzIGZsYWcgY2FuIGJlIHVzZWQgYnkgZnVuY3Rpb25hbGl0eSB0aGF0IGxvYWRzIHRoaXMgcGx1Z2luJ3Mgc2V0dGluZ3NcbiAgICAgKiBmcm9tIHRoZSByZWdpc3RyeS4gRm9yIGV4YW1wbGUsIHRoZSBzZXR0aW5nIGVkaXRvciBkb2VzIG5vdCBkaXNwbGF5IGFcbiAgICAgKiBwbHVnaW4ncyBzZXR0aW5ncyBpZiBpdCBpcyBzZXQgdG8gYHRydWVgLlxuICAgICAqL1xuICAgICdqdXB5dGVyLmxhYi5zZXR0aW5nLWRlcHJlY2F0ZWQnPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBKdXB5dGVyTGFiIGljb24gaGludC5cbiAgICAgKi9cbiAgICAnanVweXRlci5sYWIuc2V0dGluZy1pY29uJz86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBKdXB5dGVyTGFiIGljb24gY2xhc3MgaGludC5cbiAgICAgKi9cbiAgICAnanVweXRlci5sYWIuc2V0dGluZy1pY29uLWNsYXNzJz86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBKdXB5dGVyTGFiIGljb24gbGFiZWwgaGludC5cbiAgICAgKi9cbiAgICAnanVweXRlci5sYWIuc2V0dGluZy1pY29uLWxhYmVsJz86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIFRoZSBKdXB5dGVyTGFiIHRvb2xiYXJzIGNyZWF0ZWQgYnkgYSBwbHVnaW4ncyBzY2hlbWEuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogVGhlIHRvb2xiYXIgaXRlbXMgYXJlIGdyb3VwZWQgYnkgZG9jdW1lbnQgb3Igd2lkZ2V0IGZhY3RvcnkgbmFtZVxuICAgICAqIHRoYXQgd2lsbCBjb250YWluIGEgdG9vbGJhci5cbiAgICAgKi9cbiAgICAnanVweXRlci5sYWIudG9vbGJhcnMnPzogeyBbZmFjdG9yeTogc3RyaW5nXTogSVRvb2xiYXJJdGVtW10gfTtcblxuICAgIC8qKlxuICAgICAqIEEgZmxhZyB0aGF0IGluZGljYXRlcyBwbHVnaW4gc2hvdWxkIGJlIHRyYW5zZm9ybWVkIGJlZm9yZSBiZWluZyB1c2VkIGJ5XG4gICAgICogdGhlIHNldHRpbmcgcmVnaXN0cnkuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogSWYgdGhpcyB2YWx1ZSBpcyBzZXQgdG8gYHRydWVgLCB0aGUgc2V0dGluZyByZWdpc3RyeSB3aWxsIHdhaXQgdW50aWwgYVxuICAgICAqIHRyYW5zZm9ybWF0aW9uIGhhcyBiZWVuIHJlZ2lzdGVyZWQgKGJ5IGNhbGxpbmcgdGhlIGB0cmFuc2Zvcm0oKWAgbWV0aG9kXG4gICAgICogb2YgdGhlIHJlZ2lzdHJ5KSBmb3IgdGhlIHBsdWdpbiBJRCBiZWZvcmUgcmVzb2x2aW5nIGBsb2FkKClgIHByb21pc2VzLlxuICAgICAqIFRoaXMgbWVhbnMgdGhhdCBpZiB0aGUgYXR0cmlidXRlIGlzIHNldCB0byBgdHJ1ZWAgYnV0IG5vIHRyYW5zZm9ybWF0aW9uXG4gICAgICogaXMgcmVnaXN0ZXJlZCBpbiB0aW1lLCBjYWxscyB0byBgbG9hZCgpYCBhIHBsdWdpbiB3aWxsIGV2ZW50dWFsbHkgdGltZVxuICAgICAqIG91dCBhbmQgcmVqZWN0LlxuICAgICAqL1xuICAgICdqdXB5dGVyLmxhYi50cmFuc2Zvcm0nPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBKdXB5dGVyTGFiIHNob3J0Y3V0cyB0aGF0IGFyZSBjcmVhdGVkIGJ5IGEgcGx1Z2luJ3Mgc2NoZW1hLlxuICAgICAqL1xuICAgICdqdXB5dGVyLmxhYi5zaG9ydGN1dHMnPzogSVNob3J0Y3V0W107XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcm9vdCBzY2hlbWEgaXMgYWx3YXlzIGFuIG9iamVjdC5cbiAgICAgKi9cbiAgICB0eXBlOiAnb2JqZWN0JztcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgc2V0dGluZyB2YWx1ZXMgZm9yIGEgcGx1Z2luLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJU2V0dGluZ0J1bmRsZSBleHRlbmRzIFBhcnRpYWxKU09OT2JqZWN0IHtcbiAgICAvKipcbiAgICAgKiBBIGNvbXBvc2l0ZSBvZiB0aGUgdXNlciBzZXR0aW5nIHZhbHVlcyBhbmQgdGhlIHBsdWdpbiBzY2hlbWEgZGVmYXVsdHMuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogVGhlIGBjb21wb3NpdGVgIHZhbHVlcyB3aWxsIGFsd2F5cyBiZSBhIHN1cGVyc2V0IG9mIHRoZSBgdXNlcmAgdmFsdWVzLlxuICAgICAqL1xuICAgIGNvbXBvc2l0ZTogUGFydGlhbEpTT05PYmplY3Q7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgdXNlciBzZXR0aW5nIHZhbHVlcy5cbiAgICAgKi9cbiAgICB1c2VyOiBQYXJ0aWFsSlNPTk9iamVjdDtcbiAgfVxuXG4gIC8qKlxuICAgKiBBbiBpbnRlcmZhY2UgZm9yIG1hbmlwdWxhdGluZyB0aGUgc2V0dGluZ3Mgb2YgYSBzcGVjaWZpYyBwbHVnaW4uXG4gICAqL1xuICBleHBvcnQgaW50ZXJmYWNlIElTZXR0aW5ncyBleHRlbmRzIElEaXNwb3NhYmxlIHtcbiAgICAvKipcbiAgICAgKiBBIHNpZ25hbCB0aGF0IGVtaXRzIHdoZW4gdGhlIHBsdWdpbidzIHNldHRpbmdzIGhhdmUgY2hhbmdlZC5cbiAgICAgKi9cbiAgICByZWFkb25seSBjaGFuZ2VkOiBJU2lnbmFsPHRoaXMsIHZvaWQ+O1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbXBvc2l0ZSBvZiB1c2VyIHNldHRpbmdzIGFuZCBleHRlbnNpb24gZGVmYXVsdHMuXG4gICAgICovXG4gICAgcmVhZG9ubHkgY29tcG9zaXRlOiBSZWFkb25seVBhcnRpYWxKU09OT2JqZWN0O1xuXG4gICAgLyoqXG4gICAgICogVGhlIHBsdWdpbidzIElELlxuICAgICAqL1xuICAgIHJlYWRvbmx5IGlkOiBzdHJpbmc7XG5cbiAgICAvKlxuICAgICAqIFRoZSB1bmRlcmx5aW5nIHBsdWdpbi5cbiAgICAgKi9cbiAgICByZWFkb25seSBwbHVnaW46IElTZXR0aW5nUmVnaXN0cnkuSVBsdWdpbjtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwbHVnaW4gc2V0dGluZ3MgcmF3IHRleHQgdmFsdWUuXG4gICAgICovXG4gICAgcmVhZG9ubHkgcmF3OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcGx1Z2luJ3Mgc2NoZW1hLlxuICAgICAqL1xuICAgIHJlYWRvbmx5IHNjaGVtYTogSVNldHRpbmdSZWdpc3RyeS5JU2NoZW1hO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHVzZXIgc2V0dGluZ3MuXG4gICAgICovXG4gICAgcmVhZG9ubHkgdXNlcjogUmVhZG9ubHlQYXJ0aWFsSlNPTk9iamVjdDtcblxuICAgIC8qKlxuICAgICAqIFRoZSBwdWJsaXNoZWQgdmVyc2lvbiBvZiB0aGUgTlBNIHBhY2thZ2UgY29udGFpbmluZyB0aGVzZSBzZXR0aW5ncy5cbiAgICAgKi9cbiAgICByZWFkb25seSB2ZXJzaW9uOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBSZXR1cm4gdGhlIGRlZmF1bHRzIGluIGEgY29tbWVudGVkIEpTT04gZm9ybWF0LlxuICAgICAqL1xuICAgIGFubm90YXRlZERlZmF1bHRzKCk6IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIENhbGN1bGF0ZSB0aGUgZGVmYXVsdCB2YWx1ZSBvZiBhIHNldHRpbmcgYnkgaXRlcmF0aW5nIHRocm91Z2ggdGhlIHNjaGVtYS5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBrZXkgLSBUaGUgbmFtZSBvZiB0aGUgc2V0dGluZyB3aG9zZSBkZWZhdWx0IHZhbHVlIGlzIGNhbGN1bGF0ZWQuXG4gICAgICpcbiAgICAgKiBAcmV0dXJucyBBIGNhbGN1bGF0ZWQgZGVmYXVsdCBKU09OIHZhbHVlIGZvciBhIHNwZWNpZmljIHNldHRpbmcuXG4gICAgICovXG4gICAgZGVmYXVsdChrZXk6IHN0cmluZyk6IFBhcnRpYWxKU09OVmFsdWUgfCB1bmRlZmluZWQ7XG5cbiAgICAvKipcbiAgICAgKiBHZXQgYW4gaW5kaXZpZHVhbCBzZXR0aW5nLlxuICAgICAqXG4gICAgICogQHBhcmFtIGtleSAtIFRoZSBuYW1lIG9mIHRoZSBzZXR0aW5nIGJlaW5nIHJldHJpZXZlZC5cbiAgICAgKlxuICAgICAqIEByZXR1cm5zIFRoZSBzZXR0aW5nIHZhbHVlLlxuICAgICAqL1xuICAgIGdldChrZXk6IHN0cmluZyk6IHtcbiAgICAgIGNvbXBvc2l0ZTogUmVhZG9ubHlQYXJ0aWFsSlNPTlZhbHVlIHwgdW5kZWZpbmVkO1xuICAgICAgdXNlcjogUmVhZG9ubHlQYXJ0aWFsSlNPTlZhbHVlIHwgdW5kZWZpbmVkO1xuICAgIH07XG5cbiAgICAvKipcbiAgICAgKiBSZW1vdmUgYSBzaW5nbGUgc2V0dGluZy5cbiAgICAgKlxuICAgICAqIEBwYXJhbSBrZXkgLSBUaGUgbmFtZSBvZiB0aGUgc2V0dGluZyBiZWluZyByZW1vdmVkLlxuICAgICAqXG4gICAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2hlbiB0aGUgc2V0dGluZyBpcyByZW1vdmVkLlxuICAgICAqXG4gICAgICogIyMjIyBOb3Rlc1xuICAgICAqIFRoaXMgZnVuY3Rpb24gaXMgYXN5bmNocm9ub3VzIGJlY2F1c2UgaXQgd3JpdGVzIHRvIHRoZSBzZXR0aW5nIHJlZ2lzdHJ5LlxuICAgICAqL1xuICAgIHJlbW92ZShrZXk6IHN0cmluZyk6IFByb21pc2U8dm9pZD47XG5cbiAgICAvKipcbiAgICAgKiBTYXZlIGFsbCBvZiB0aGUgcGx1Z2luJ3MgdXNlciBzZXR0aW5ncyBhdCBvbmNlLlxuICAgICAqL1xuICAgIHNhdmUocmF3OiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+O1xuXG4gICAgLyoqXG4gICAgICogU2V0IGEgc2luZ2xlIHNldHRpbmcuXG4gICAgICpcbiAgICAgKiBAcGFyYW0ga2V5IC0gVGhlIG5hbWUgb2YgdGhlIHNldHRpbmcgYmVpbmcgc2V0LlxuICAgICAqXG4gICAgICogQHBhcmFtIHZhbHVlIC0gVGhlIHZhbHVlIG9mIHRoZSBzZXR0aW5nLlxuICAgICAqXG4gICAgICogQHJldHVybnMgQSBwcm9taXNlIHRoYXQgcmVzb2x2ZXMgd2hlbiB0aGUgc2V0dGluZyBoYXMgYmVlbiBzYXZlZC5cbiAgICAgKlxuICAgICAqICMjIyMgTm90ZXNcbiAgICAgKiBUaGlzIGZ1bmN0aW9uIGlzIGFzeW5jaHJvbm91cyBiZWNhdXNlIGl0IHdyaXRlcyB0byB0aGUgc2V0dGluZyByZWdpc3RyeS5cbiAgICAgKi9cbiAgICBzZXQoa2V5OiBzdHJpbmcsIHZhbHVlOiBQYXJ0aWFsSlNPTlZhbHVlKTogUHJvbWlzZTx2b2lkPjtcblxuICAgIC8qKlxuICAgICAqIFZhbGlkYXRlcyByYXcgc2V0dGluZ3Mgd2l0aCBjb21tZW50cy5cbiAgICAgKlxuICAgICAqIEBwYXJhbSByYXcgLSBUaGUgSlNPTiB3aXRoIGNvbW1lbnRzIHN0cmluZyBiZWluZyB2YWxpZGF0ZWQuXG4gICAgICpcbiAgICAgKiBAcmV0dXJucyBBIGxpc3Qgb2YgZXJyb3JzIG9yIGBudWxsYCBpZiB2YWxpZC5cbiAgICAgKi9cbiAgICB2YWxpZGF0ZShyYXc6IHN0cmluZyk6IElTY2hlbWFWYWxpZGF0b3IuSUVycm9yW10gfCBudWxsO1xuICB9XG5cbiAgLyoqXG4gICAqIEFuIGludGVyZmFjZSBkZXNjcmliaW5nIGEgSnVweXRlckxhYiBrZXlib2FyZCBzaG9ydGN1dC5cbiAgICovXG4gIGV4cG9ydCBpbnRlcmZhY2UgSVNob3J0Y3V0IGV4dGVuZHMgUGFydGlhbEpTT05PYmplY3Qge1xuICAgIC8qKlxuICAgICAqIFRoZSBvcHRpb25hbCBhcmd1bWVudHMgcGFzc2VkIGludG8gdGhlIHNob3J0Y3V0J3MgY29tbWFuZC5cbiAgICAgKi9cbiAgICBhcmdzPzogUGFydGlhbEpTT05PYmplY3Q7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgY29tbWFuZCBpbnZva2VkIGJ5IHRoZSBzaG9ydGN1dC5cbiAgICAgKi9cbiAgICBjb21tYW5kOiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBXaGV0aGVyIGEga2V5Ym9hcmQgc2hvcnRjdXQgaXMgZGlzYWJsZWQuIGBGYWxzZWAgYnkgZGVmYXVsdC5cbiAgICAgKi9cbiAgICBkaXNhYmxlZD86IGJvb2xlYW47XG5cbiAgICAvKipcbiAgICAgKiBUaGUga2V5IHNlcXVlbmNlIG9mIHRoZSBzaG9ydGN1dC5cbiAgICAgKlxuICAgICAqICMjIyBOb3Rlc1xuICAgICAqXG4gICAgICogSWYgdGhpcyBpcyBhIGxpc3QgbGlrZSBgWydDdHJsIEEnLCAnQiddYCwgdGhlIHVzZXIgbmVlZHMgdG8gcHJlc3NcbiAgICAgKiBgQ3RybCBBYCBmb2xsb3dlZCBieSBgQmAgdG8gdHJpZ2dlciB0aGUgc2hvcnRjdXRzLlxuICAgICAqL1xuICAgIGtleXM6IHN0cmluZ1tdO1xuXG4gICAgLyoqXG4gICAgICogVGhlIENTUyBzZWxlY3RvciBhcHBsaWNhYmxlIHRvIHRoZSBzaG9ydGN1dC5cbiAgICAgKi9cbiAgICBzZWxlY3Rvcjogc3RyaW5nO1xuICB9XG5cbiAgLyoqXG4gICAqIEFuIGludGVyZmFjZSBkZXNjcmliaW5nIGEgdG9vbGJhciBpdGVtLlxuICAgKi9cbiAgZXhwb3J0IGludGVyZmFjZSBJVG9vbGJhckl0ZW0gZXh0ZW5kcyBQYXJ0aWFsSlNPTk9iamVjdCB7XG4gICAgLyoqXG4gICAgICogVW5pcXVlIHRvb2xiYXIgaXRlbSBuYW1lXG4gICAgICovXG4gICAgbmFtZTogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGNvbW1hbmQgdG8gZXhlY3V0ZSB3aGVuIHRoZSBpdGVtIGlzIHRyaWdnZXJlZC5cbiAgICAgKlxuICAgICAqIFRoZSBkZWZhdWx0IHZhbHVlIGlzIGFuIGVtcHR5IHN0cmluZy5cbiAgICAgKi9cbiAgICBjb21tYW5kPzogc3RyaW5nO1xuXG4gICAgLyoqXG4gICAgICogVGhlIGFyZ3VtZW50cyBmb3IgdGhlIGNvbW1hbmQuXG4gICAgICpcbiAgICAgKiBUaGUgZGVmYXVsdCB2YWx1ZSBpcyBhbiBlbXB0eSBvYmplY3QuXG4gICAgICovXG4gICAgYXJncz86IFBhcnRpYWxKU09OT2JqZWN0O1xuXG4gICAgLyoqXG4gICAgICogV2hldGhlciB0aGUgdG9vbGJhciBpdGVtIGlzIGlnbm9yZWQgKGkuZS4gbm90IGNyZWF0ZWQpLiBgZmFsc2VgIGJ5IGRlZmF1bHQuXG4gICAgICpcbiAgICAgKiAjIyMjIE5vdGVzXG4gICAgICogVGhpcyBhbGxvd3MgYW4gdXNlciB0byBzdXBwcmVzcyB0b29sYmFyIGl0ZW1zLlxuICAgICAqL1xuICAgIGRpc2FibGVkPzogYm9vbGVhbjtcblxuICAgIC8qKlxuICAgICAqIEl0ZW0gaWNvbiBpZFxuICAgICAqXG4gICAgICogIyMjIyBOb3RlXG4gICAgICogVGhlIGlkIHdpbGwgYmUgbG9va2VkIGZvciBpbiB0aGUgTGFiSWNvbiByZWdpc3RyeS5cbiAgICAgKiBUaGUgY29tbWFuZCBpY29uIHdpbGwgYmUgb3ZlcnJpZGRlbiBieSB0aGlzIGxhYmVsIGlmIGRlZmluZWQuXG4gICAgICovXG4gICAgaWNvbj86IHN0cmluZztcblxuICAgIC8qKlxuICAgICAqIEl0ZW0gbGFiZWxcbiAgICAgKlxuICAgICAqICMjIyMgTm90ZVxuICAgICAqIFRoZSBjb21tYW5kIGxhYmVsIHdpbGwgYmUgb3ZlcnJpZGRlbiBieSB0aGlzIGxhYmVsIGlmIGRlZmluZWQuXG4gICAgICovXG4gICAgbGFiZWw/OiBzdHJpbmc7XG5cbiAgICAvKipcbiAgICAgKiBUaGUgcmFuayBvcmRlciBvZiB0aGUgdG9vbGJhciBpdGVtIGFtb25nIGl0cyBzaWJsaW5ncy5cbiAgICAgKi9cbiAgICByYW5rPzogbnVtYmVyO1xuXG4gICAgLyoqXG4gICAgICogVGhlIHR5cGUgb2YgdGhlIHRvb2xiYXIgaXRlbS5cbiAgICAgKi9cbiAgICB0eXBlPzogJ2NvbW1hbmQnIHwgJ3NwYWNlcic7XG4gIH1cbn1cbiJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==