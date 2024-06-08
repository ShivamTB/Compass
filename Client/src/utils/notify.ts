import { Notify } from 'quasar'

export const notify = (message: string, type: 'positive' | 'negative' | 'warning' | 'info' = 'info') => {
    Notify.create({
        message,
        type,
        icon: type === 'positive' ? 'check' : type === 'negative' ? 'close' : type === 'warning' ? 'warning' : 'info',
        position: 'bottom',
        timeout: 2000
    })
}

export const notifyError = (message: string) => {
    notify(message, 'negative')
}

export const notifySuccess = (message: string) => {
    notify(message, 'positive')
}

export const notifyWarning = (message: string) => {
    notify(message, 'warning')
}

export const notifyInfo = (message: string) => {
    notify(message, 'info')
}

