local ls = require("luasnip")
local fmt = require('luasnip.extras.fmt').fmt
-- some shorthands...
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node

-- general func()
ls.add_snippets('c', {
    s("fn", {
        t( "// Arguments: " ),
        t({ "", "void func() {" }),
        t({ "", "\t" }),
        i(1),
        t({ "", "}" }),
    })
})

-- main
ls.add_snippets('c', {
    s("main", {
        t({ "#include <stdio.h>" }),
        t({ "", "" }),
        t({ "", "int main() {" }),
        t({ "", "\t" }),
        i(1),
        t({ "", "\treturn 0;"}),
        t({ "", "}" }),
    })
})
