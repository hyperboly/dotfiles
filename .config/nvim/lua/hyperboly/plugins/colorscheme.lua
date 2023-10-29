return {
    "folke/tokyonight.nvim",
    lazy = false,
    priority = 1000,
    opts = {
        transparent = true,
        style = "storm",
        styles = {
            italic = "true",
            sidebars = "transparent",
            floats = "transparent",
        },
    },
    config = function()
        vim.cmd[[colorscheme tokyonight-storm]]
    end,
}
