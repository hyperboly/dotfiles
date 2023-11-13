-- return {
--     "folke/tokyonight.nvim",
--     lazy = false,
--     priority = 1000,
--     opts = {
--         transparent = true,
--         style = "storm",
--         styles = {
--             italic = "true",
--             sidebars = "transparent",
--             floats = "transparent",
--         },
--     },
--     config = function()
--         vim.cmd[[colorscheme tokyonight-storm]]
--     end,
-- }

return {
    "catppuccin/nvim",
    name = "catppuccin",
    priority = 1000,
    opts = {
        term_colors = true,
        transparent_background = true,
        styles = { -- Handles the styles of general hi groups (see `:h highlight-args`):
            comments = { "italic" }, -- Change the style of comments
            conditionals = { "italic" },
        },
    },
    config = function()
        vim.cmd[[colorscheme catppuccin-macchiato]]
    end,
}
