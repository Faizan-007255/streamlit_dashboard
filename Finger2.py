import {
    useCallback,
    useEffect,
    useState
} from "react";

declare global {
    interface Window {
        Fingerprint: any;
    }
}

interface Props {
    fingerPrint: string;
    handleFinger: (image: string) => void;
}

const useFingerPrintReader = ({
    fingerPrint,
    handleFinger
}: Props) => {
    const [sdk, setSdk] = useState < any > (null);
    const [imageSrc, setImageSrc] = useState(fingerPrint || "");
    const [isCapturing, setIsCapturing] = useState(false);

    const setFingerPrint = useCallback((fingerprint: string) => handleFinger(fingerprint), [handleFinger]);

    useEffect(() => {
        if (typeof window !== "undefined") {
            const sdkInstance = new window.Fingerprint.WebApi();

            sdkInstance.onSamplesAcquired = (s: any) => {
                const samples = JSON.parse(s.samples);
                const base64 = `data:image/png;base64,${window.Fingerprint.b64UrlTo64(samples[0])}`;
                setImageSrc(base64);
                setFingerPrint(base64);
                stopCapture(sdkInstance);
            };

            setSdk(sdkInstance);

            return () => {
                sdkInstance.stopAcquisition().catch(() => {
                    console.warn("Error al detener la captura de huella en cleanup");
                });
            };
        } else {
            console.warn("Fingerprint SDK no está disponible en el objeto `window`.");
        }
    }, [setFingerPrint]);

    const startCapture = async () => {
        if (sdk) {
            await sdk.startAcquisition(window.Fingerprint.SampleFormat.PngImage).then(
                () => console.log("Capturando huella"),
                () => console.error("Error al comenzar la captura de huella")
            );
            setIsCapturing(true);
        } else {
            console.warn("El SDK de huellas no está inicializado.");
        }
    };

    const stopCapture = async (sdkInstance: any) => {
        if (sdkInstance) {
            await sdkInstance.stopAcquisition().then(
                () => console.log("Captura de huella detenida"),
                () => console.error("Error al detener la captura de huella")
            );
            setIsCapturing(false);
        }
    };

    return {
        startCapture,
        isCapturing,
        imageSrc,
    };
};