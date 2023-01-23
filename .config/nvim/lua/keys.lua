function map(mode, lhs, rhs, opts)
    local options = { noremap = true }
    if opts then
        options = vim.tbl_extend("force", options, opts)
    end
    vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end

map("n", "<Leader>c", ":! pdflatex %<CR><CR>", { silent = true })

map("n", "F3", ":!texcount % -inc -incbib -sum -1<CR><CR>")

vim.g.mapleader = " "
