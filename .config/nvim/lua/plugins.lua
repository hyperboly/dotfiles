-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
  -- Packer can manage itself
    use 'wbthomason/packer.nvim'
    use 'vimwiki/vimwiki'
    use 'rstacruz/vim-closer'
    use 'vim-airline/vim-airline'
    use 'vim-airline/vim-airline-themes'
    use 'mhinz/vim-startify'
end)
