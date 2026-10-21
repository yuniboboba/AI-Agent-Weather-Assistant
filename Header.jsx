import { Menu, Button } from 'antd'
import { MenuOutlined } from '@ant-design/icons'
import { useState } from 'react'

function HeaderNav() {
  const menuItems = [
    { key: 'agent', label: 'Agent' },
    { key: 'dashboard', label: 'Dashboard' },
    { key: 'history', label: 'History' },
    { key: 'memory', label: 'Memory' },
    { key: 'settings', label: 'Settings' },
  ]

  const [open, setOpen] = useState(false)

  function toggleMenu() {
    setOpen(!open)
  }

  return (
    <header className="sticky top-0 z-50 flex h-16 items-center bg-slate-900 px-4 shadow-lg md:px-8">
      {/* 左側 Logo / 專案名 */}
      <div className="mr-10 flex h-9 min-w-[180px] items-center justify-center rounded-xl bg-slate-700 text-sm font-semibold text-white">
        WeatherMate AI
      </div>

      {/* 中間導航列 */}
      <div className='hidden flex-1 md:block'>
        <Menu
          mode="horizontal"
          items={menuItems}
          defaultSelectedKeys={['dashboard']}
          className="border-none bg-transparent text-white"
          theme="dark"
        />
      </div>

      {/* 右側簡單狀態 */}
      <div className="hidden ml-8 text-sm text-slate-300 md:block">
        Tokyo
      </div>
      <div className='relative ml-auto mr-4 md:hidden'>
        <Button
          type="text"
          icon={<MenuOutlined />}
          onClick={toggleMenu}
          className="!text-white"
        />

        {/* 小螢幕下拉菜單 */}
        {open && (
          <div className="absolute right-0.5 top-full border-t border-slate-700 pb-4">
            <Menu
              mode="vertical"
              items={menuItems}
              defaultSelectedKeys={['dashboard']}
              theme="dark"
              className="border-none bg-slate-900"
              onClick={() => setOpen(false)}
            />
          </div>
        )}
      </div>

    </header>
  )
}

export default HeaderNav