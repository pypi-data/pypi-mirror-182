var _a, _b;
import { Model } from "../../model";
import * as dom from "../../core/dom";
export class StyleSheet extends Model {
    constructor(attrs) {
        super(attrs);
    }
}
StyleSheet.__name__ = "StyleSheet";
export class InlineStyleSheet extends StyleSheet {
    constructor(attrs) {
        super(attrs);
    }
    underlying() {
        return new dom.InlineStyleSheet(this.css);
    }
}
_a = InlineStyleSheet;
InlineStyleSheet.__name__ = "InlineStyleSheet";
(() => {
    _a.define(({ String }) => ({
        css: [String],
    }));
})();
export class ImportedStyleSheet extends StyleSheet {
    constructor(attrs) {
        super(attrs);
    }
    underlying() {
        return new dom.ImportedStyleSheet(this.url);
    }
}
_b = ImportedStyleSheet;
ImportedStyleSheet.__name__ = "ImportedStyleSheet";
(() => {
    _b.define(({ String }) => ({
        url: [String],
    }));
})();
export class GlobalInlineStyleSheet extends InlineStyleSheet {
    constructor(attrs) {
        super(attrs);
        this._underlying = null;
    }
    underlying() {
        if (this._underlying == null)
            this._underlying = new dom.GlobalInlineStyleSheet(this.css);
        return this._underlying;
    }
}
GlobalInlineStyleSheet.__name__ = "GlobalInlineStyleSheet";
export class GlobalImportedStyleSheet extends ImportedStyleSheet {
    constructor(attrs) {
        super(attrs);
        this._underlying = null;
    }
    underlying() {
        if (this._underlying == null)
            this._underlying = new dom.GlobalInlineStyleSheet(this.url);
        return this._underlying;
    }
}
GlobalImportedStyleSheet.__name__ = "GlobalImportedStyleSheet";
//# sourceMappingURL=stylesheets.js.map